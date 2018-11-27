# Copyright 2016, 2017 Intel Corporation
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ------------------------------------------------------------------------------

import asyncio
import re
import logging
import json
import base64
import hashlib
import random

from aiohttp import web

# pylint: disable=no-name-in-module,import-error
# needed for the google.protobuf imports to pass pylint
from google.protobuf.json_format import MessageToDict
from google.protobuf.message import DecodeError

from sawtooth_rest_api.protobuf.validator_pb2 import Message

import sawtooth_rest_api.exceptions as errors
from sawtooth_rest_api import error_handlers
from sawtooth_rest_api.messaging import DisconnectError
from sawtooth_rest_api.messaging import SendBackoffTimeoutError
from sawtooth_rest_api.protobuf import client_transaction_pb2
from sawtooth_rest_api.protobuf import client_list_control_pb2
from sawtooth_rest_api.protobuf import client_batch_submit_pb2
from sawtooth_rest_api.protobuf import client_state_pb2
from sawtooth_rest_api.protobuf import client_block_pb2
from sawtooth_rest_api.protobuf import client_batch_pb2
from sawtooth_rest_api.protobuf import client_receipt_pb2
from sawtooth_rest_api.protobuf import client_peers_pb2
from sawtooth_rest_api.protobuf import client_status_pb2
from sawtooth_rest_api.protobuf.block_pb2 import BlockHeader
from sawtooth_rest_api.protobuf.batch_pb2 import Batch,BatchHeader,BatchList
from sawtooth_rest_api.protobuf.transaction_pb2 import Transaction,TransactionHeader

from sawtooth_rest_api.route_handlers import RouteHandler,DEFAULT_TIMEOUT
import cbor

from sawtooth_signing.secp256k1 import Secp256k1PrivateKey, Secp256k1PublicKey, Secp256k1Context
from sawtooth_signing import CryptoFactory,create_context

from smart_bgt.processor.utils import FAMILY_NAME as SMART_BGX_FAMILY
from smart_bgt.processor.utils import FAMILY_VER as SMART_BGX_VER
from smart_bgt.processor.utils import make_smart_bgt_address

LOGGER = logging.getLogger(__name__)

def _sha512(data):
    return hashlib.sha512(data).hexdigest()

def _base64url2public(addr):
    return addr

def _public2base64url(key):
    return key

class BgxRouteHandler(RouteHandler):
    """Contains a number of aiohttp handlers for endpoints in the Rest Api.

    Each handler takes an aiohttp Request object, and uses the data in
    that request to send Protobuf message to a validator. The Protobuf response
    is then parsed, and finally an aiohttp Response object is sent back
    to the client with JSON formatted data and metadata.

    If something goes wrong, an aiohttp HTTP exception is raised or returned
    instead.

    Args:
        connection (:obj: messaging.Connection): The object that communicates
            with the validator.
        timeout (int, optional): The time in seconds before the Api should
            cancel a request and report that the validator is unavailable.
    """

    def __init__(self, loop, connection,timeout=DEFAULT_TIMEOUT, metrics_registry=None):

        super().__init__(loop,connection,timeout,metrics_registry)
        # BGX init
        self._context = create_context('secp256k1') 
        self._private_key = Secp256k1PrivateKey.new_random()
        self._public_key = self._context.get_public_key(self._private_key)
        self._crypto_factory = CryptoFactory(self._context)
        self._signer = self._crypto_factory.new_signer(self._private_key)
        LOGGER.debug('BgxRouteHandler: _signer PUBLIC_KEY=%s',self._public_key.as_hex())

    def _create_batch(self, transactions):
        """
        Create batch for transactions
        """
        transaction_signatures = [t.header_signature for t in transactions]

        header = BatchHeader(
            signer_public_key=self._signer.get_public_key().as_hex(),
            transaction_ids=transaction_signatures
        ).SerializeToString()

        signature = self._signer.sign(header)

        batch = Batch(
            header=header,
            transactions=transactions,
            header_signature=signature)
        return batch
        #return BatchList(batches=[batch])

    def _create_transaction(self,payload,inputs,outputs,dependencies=[]):
        """
        make transaction
        """
        LOGGER.debug('BgxRouteHandler: _create_transaction make Transaction')
        txn_header = TransactionHeader(
            signer_public_key=self._signer.get_public_key().as_hex(),
            family_name=SMART_BGX_FAMILY,
            family_version=SMART_BGX_VER,
            inputs=inputs,
            outputs=outputs,
            dependencies=dependencies,
            payload_sha512=_sha512(payload),
            batcher_public_key=self._signer.get_public_key().as_hex(),
            nonce=hex(random.randint(0, 2**64))
        ).SerializeToString()

        signature = self._signer.sign(txn_header)
        transaction = Transaction(
            header=txn_header,
            payload=payload,
            header_signature=signature
        )
        return transaction

    async def post_transfer(self, request):
        """
        make transfer from wallet to wallet
        """
        LOGGER.debug('BgxRouteHandler: post_transfer !!!')
        timer_ctx = self._post_batches_total_time.time()
        self._post_batches_count.inc()
        body = await request.json()

        LOGGER.debug('BgxRouteHandler: post_transfer body=(%s)',body)
        if 'data' not in body:
            raise errors.NoTransactionPayload()

        data = body['data']
        try:
            signed_payload = data['signed_payload']
            payload = data['payload']
            address_from = payload['address_from']
            address_to = payload['address_to']
            num_bgt    = payload['tx_payload']

        except KeyError:
            raise errors.BadTransactionPayload()

        # TODO !!!
        # convert from base64url addr 
        address_from =  _base64url2public(address_from)
        address_to   =  _base64url2public(address_to)
        # Verification of signed hashes
        """
        result = rest_api_utils.verify_signature(public_key_from, signed_payload, payload)
        if result != 1:
            raise errors.InvalidSignature()
        """
        LOGGER.debug('BgxRouteHandler: post_transaction make payload=%s',payload)
        payload_bytes = cbor.dumps({
            'Verb'   : 'transfer',
            'Name'   : address_from,
            'to_addr': address_to,
            'num_bgt': num_bgt,
        })
       
        in_address = make_smart_bgt_address(address_from)
        out_address = make_smart_bgt_address(address_to)
        inputs =[in_address, out_address]   
        outputs=[in_address, out_address]
        transaction = self._create_transaction(payload_bytes,inputs,outputs)
        batch = self._create_batch([transaction])
        batch_id = batch.header_signature #batch_list.batches[0].header_signature

        # Query validator
        error_traps = [error_handlers.BatchInvalidTrap,error_handlers.BatchQueueFullTrap]
        validator_query = client_batch_submit_pb2.ClientBatchSubmitRequest(batches=[batch])
        LOGGER.debug('BgxRouteHandler: post_transfer send batch_id=%s',batch_id)

        with self._post_batches_validator_time.time():
            await self._query_validator(
                Message.CLIENT_BATCH_SUBMIT_REQUEST,
                client_batch_submit_pb2.ClientBatchSubmitResponse,
                validator_query,
                error_traps)

        # Build response envelope
        status = 202
        link = self._build_url(request, path='/batch_statuses', id=batch_id)

        retval = self._wrap_response(
            request,
            metadata={'link': link},
            status=status)
        LOGGER.debug('BgxRouteHandler: post_transfer retval=%s',retval)
        timer_ctx.stop()
        return retval


    async def get_wallet(self, request):
        """
        get wallet balance
        """
        address = request.match_info.get('address', '')
        address =  _base64url2public(address)
        LOGGER.debug('BgxRouteHandler: get_wallet address=%s',address)
        token_address = make_smart_bgt_address(address)

        error_traps = [
            error_handlers.InvalidAddressTrap,
            error_handlers.StateNotFoundTrap]

        head = request.url.query.get('head', None)

        head, root = await self._head_to_root(head)
        response = await self._query_validator(
            Message.CLIENT_STATE_GET_REQUEST,
            client_state_pb2.ClientStateGetResponse,
            client_state_pb2.ClientStateGetRequest(
                state_root=root, address=token_address),
            error_traps)

        try:
            result = cbor.loads(base64.b64decode(response['value']))
            LOGGER.debug('BgxRouteHandler: get_wallet result=%s',result)
        except BaseException:
            return None

        return self._wrap_response(
            request,
            data=result)

    # First iteration of implementation
    async def post_wallet(self, request):
        """
        create wallet
        """
        if 'public_key' not in request.headers:
            LOGGER.debug('Submission header public_key is mandatory')
            raise errors.NoMandatoryHeader()
        public_key = request.headers['public_key']

        # convert  public_key to base64url for using it into url /wallets/addr
        user_address = _public2base64url(public_key)

       
        return self._wrap_response(
            request,
            metadata={
                user_address: {
                    'wallet': {}
                }
            },
            status=200)



