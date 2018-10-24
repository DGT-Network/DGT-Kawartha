# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: sawtooth_sdk/protobuf/transaction.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='sawtooth_sdk/protobuf/transaction.proto',
  package='',
  syntax='proto3',
  serialized_pb=_b('\n\'sawtooth_sdk/protobuf/transaction.proto\"\xd5\x01\n\x11TransactionHeader\x12\x1a\n\x12\x62\x61tcher_public_key\x18\x01 \x01(\t\x12\x14\n\x0c\x64\x65pendencies\x18\x02 \x03(\t\x12\x13\n\x0b\x66\x61mily_name\x18\x03 \x01(\t\x12\x16\n\x0e\x66\x61mily_version\x18\x04 \x01(\t\x12\x0e\n\x06inputs\x18\x05 \x03(\t\x12\r\n\x05nonce\x18\x06 \x01(\t\x12\x0f\n\x07outputs\x18\x07 \x03(\t\x12\x16\n\x0epayload_sha512\x18\t \x01(\t\x12\x19\n\x11signer_public_key\x18\n \x01(\t\"H\n\x0bTransaction\x12\x0e\n\x06header\x18\x01 \x01(\x0c\x12\x18\n\x10header_signature\x18\x02 \x01(\t\x12\x0f\n\x07payload\x18\x03 \x01(\x0c\"5\n\x0fTransactionList\x12\"\n\x0ctransactions\x18\x01 \x03(\x0b\x32\x0c.TransactionB*\n\x15sawtooth.sdk.protobufP\x01Z\x0ftransaction_pb2b\x06proto3')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_TRANSACTIONHEADER = _descriptor.Descriptor(
  name='TransactionHeader',
  full_name='TransactionHeader',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='batcher_public_key', full_name='TransactionHeader.batcher_public_key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='dependencies', full_name='TransactionHeader.dependencies', index=1,
      number=2, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='family_name', full_name='TransactionHeader.family_name', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='family_version', full_name='TransactionHeader.family_version', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='inputs', full_name='TransactionHeader.inputs', index=4,
      number=5, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='nonce', full_name='TransactionHeader.nonce', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='outputs', full_name='TransactionHeader.outputs', index=6,
      number=7, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='payload_sha512', full_name='TransactionHeader.payload_sha512', index=7,
      number=9, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='signer_public_key', full_name='TransactionHeader.signer_public_key', index=8,
      number=10, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=44,
  serialized_end=257,
)


_TRANSACTION = _descriptor.Descriptor(
  name='Transaction',
  full_name='Transaction',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='header', full_name='Transaction.header', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='header_signature', full_name='Transaction.header_signature', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='payload', full_name='Transaction.payload', index=2,
      number=3, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=259,
  serialized_end=331,
)


_TRANSACTIONLIST = _descriptor.Descriptor(
  name='TransactionList',
  full_name='TransactionList',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='transactions', full_name='TransactionList.transactions', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=333,
  serialized_end=386,
)

_TRANSACTIONLIST.fields_by_name['transactions'].message_type = _TRANSACTION
DESCRIPTOR.message_types_by_name['TransactionHeader'] = _TRANSACTIONHEADER
DESCRIPTOR.message_types_by_name['Transaction'] = _TRANSACTION
DESCRIPTOR.message_types_by_name['TransactionList'] = _TRANSACTIONLIST

TransactionHeader = _reflection.GeneratedProtocolMessageType('TransactionHeader', (_message.Message,), dict(
  DESCRIPTOR = _TRANSACTIONHEADER,
  __module__ = 'sawtooth_sdk.protobuf.transaction_pb2'
  # @@protoc_insertion_point(class_scope:TransactionHeader)
  ))
_sym_db.RegisterMessage(TransactionHeader)

Transaction = _reflection.GeneratedProtocolMessageType('Transaction', (_message.Message,), dict(
  DESCRIPTOR = _TRANSACTION,
  __module__ = 'sawtooth_sdk.protobuf.transaction_pb2'
  # @@protoc_insertion_point(class_scope:Transaction)
  ))
_sym_db.RegisterMessage(Transaction)

TransactionList = _reflection.GeneratedProtocolMessageType('TransactionList', (_message.Message,), dict(
  DESCRIPTOR = _TRANSACTIONLIST,
  __module__ = 'sawtooth_sdk.protobuf.transaction_pb2'
  # @@protoc_insertion_point(class_scope:TransactionList)
  ))
_sym_db.RegisterMessage(TransactionList)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n\025sawtooth.sdk.protobufP\001Z\017transaction_pb2'))
# @@protoc_insertion_point(module_scope)
