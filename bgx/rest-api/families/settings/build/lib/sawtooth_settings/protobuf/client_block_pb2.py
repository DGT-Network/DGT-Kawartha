# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: sawtooth_settings/protobuf/client_block.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from sawtooth_settings.protobuf import block_pb2 as sawtooth__settings_dot_protobuf_dot_block__pb2
from sawtooth_settings.protobuf import client_list_control_pb2 as sawtooth__settings_dot_protobuf_dot_client__list__control__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='sawtooth_settings/protobuf/client_block.proto',
  package='',
  syntax='proto3',
  serialized_pb=_b('\n-sawtooth_settings/protobuf/client_block.proto\x1a&sawtooth_settings/protobuf/block.proto\x1a\x34sawtooth_settings/protobuf/client_list_control.proto\"\x89\x01\n\x16\x43lientBlockListRequest\x12\x0f\n\x07head_id\x18\x01 \x01(\t\x12\x11\n\tblock_ids\x18\x02 \x03(\t\x12%\n\x06paging\x18\x03 \x01(\x0b\x32\x15.ClientPagingControls\x12$\n\x07sorting\x18\x04 \x03(\x0b\x32\x13.ClientSortControls\"\xb6\x02\n\x17\x43lientBlockListResponse\x12/\n\x06status\x18\x01 \x01(\x0e\x32\x1f.ClientBlockListResponse.Status\x12\x16\n\x06\x62locks\x18\x02 \x03(\x0b\x32\x06.Block\x12\x0f\n\x07head_id\x18\x03 \x01(\t\x12%\n\x06paging\x18\x04 \x01(\x0b\x32\x15.ClientPagingResponse\"\x99\x01\n\x06Status\x12\x10\n\x0cSTATUS_UNSET\x10\x00\x12\x06\n\x02OK\x10\x01\x12\x12\n\x0eINTERNAL_ERROR\x10\x02\x12\r\n\tNOT_READY\x10\x03\x12\x0b\n\x07NO_ROOT\x10\x04\x12\x0f\n\x0bNO_RESOURCE\x10\x05\x12\x12\n\x0eINVALID_PAGING\x10\x06\x12\x10\n\x0cINVALID_SORT\x10\x07\x12\x0e\n\nINVALID_ID\x10\x08\"-\n\x19\x43lientBlockGetByIdRequest\x12\x10\n\x08\x62lock_id\x18\x01 \x01(\t\"/\n\x1a\x43lientBlockGetByNumRequest\x12\x11\n\tblock_num\x18\x01 \x01(\x04\">\n$ClientBlockGetByTransactionIdRequest\x12\x16\n\x0etransaction_id\x18\x01 \x01(\t\"2\n\x1e\x43lientBlockGetByBatchIdRequest\x12\x10\n\x08\x62\x61tch_id\x18\x01 \x01(\t\"\xb8\x01\n\x16\x43lientBlockGetResponse\x12.\n\x06status\x18\x01 \x01(\x0e\x32\x1e.ClientBlockGetResponse.Status\x12\x15\n\x05\x62lock\x18\x02 \x01(\x0b\x32\x06.Block\"W\n\x06Status\x12\x10\n\x0cSTATUS_UNSET\x10\x00\x12\x06\n\x02OK\x10\x01\x12\x12\n\x0eINTERNAL_ERROR\x10\x02\x12\x0f\n\x0bNO_RESOURCE\x10\x05\x12\x0e\n\nINVALID_ID\x10\x08\x42+\n\x15sawtooth.sdk.protobufP\x01Z\x10\x63lient_block_pb2b\x06proto3')
  ,
  dependencies=[sawtooth__settings_dot_protobuf_dot_block__pb2.DESCRIPTOR,sawtooth__settings_dot_protobuf_dot_client__list__control__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)



_CLIENTBLOCKLISTRESPONSE_STATUS = _descriptor.EnumDescriptor(
  name='Status',
  full_name='ClientBlockListResponse.Status',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='STATUS_UNSET', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='OK', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INTERNAL_ERROR', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='NOT_READY', index=3, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='NO_ROOT', index=4, number=4,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='NO_RESOURCE', index=5, number=5,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INVALID_PAGING', index=6, number=6,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INVALID_SORT', index=7, number=7,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INVALID_ID', index=8, number=8,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=441,
  serialized_end=594,
)
_sym_db.RegisterEnumDescriptor(_CLIENTBLOCKLISTRESPONSE_STATUS)

_CLIENTBLOCKGETRESPONSE_STATUS = _descriptor.EnumDescriptor(
  name='Status',
  full_name='ClientBlockGetResponse.Status',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='STATUS_UNSET', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='OK', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INTERNAL_ERROR', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='NO_RESOURCE', index=3, number=5,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INVALID_ID', index=4, number=8,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=906,
  serialized_end=993,
)
_sym_db.RegisterEnumDescriptor(_CLIENTBLOCKGETRESPONSE_STATUS)


_CLIENTBLOCKLISTREQUEST = _descriptor.Descriptor(
  name='ClientBlockListRequest',
  full_name='ClientBlockListRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='head_id', full_name='ClientBlockListRequest.head_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='block_ids', full_name='ClientBlockListRequest.block_ids', index=1,
      number=2, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='paging', full_name='ClientBlockListRequest.paging', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='sorting', full_name='ClientBlockListRequest.sorting', index=3,
      number=4, type=11, cpp_type=10, label=3,
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
  serialized_start=144,
  serialized_end=281,
)


_CLIENTBLOCKLISTRESPONSE = _descriptor.Descriptor(
  name='ClientBlockListResponse',
  full_name='ClientBlockListResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='ClientBlockListResponse.status', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='blocks', full_name='ClientBlockListResponse.blocks', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='head_id', full_name='ClientBlockListResponse.head_id', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='paging', full_name='ClientBlockListResponse.paging', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _CLIENTBLOCKLISTRESPONSE_STATUS,
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=284,
  serialized_end=594,
)


_CLIENTBLOCKGETBYIDREQUEST = _descriptor.Descriptor(
  name='ClientBlockGetByIdRequest',
  full_name='ClientBlockGetByIdRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='block_id', full_name='ClientBlockGetByIdRequest.block_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
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
  serialized_start=596,
  serialized_end=641,
)


_CLIENTBLOCKGETBYNUMREQUEST = _descriptor.Descriptor(
  name='ClientBlockGetByNumRequest',
  full_name='ClientBlockGetByNumRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='block_num', full_name='ClientBlockGetByNumRequest.block_num', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=643,
  serialized_end=690,
)


_CLIENTBLOCKGETBYTRANSACTIONIDREQUEST = _descriptor.Descriptor(
  name='ClientBlockGetByTransactionIdRequest',
  full_name='ClientBlockGetByTransactionIdRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='transaction_id', full_name='ClientBlockGetByTransactionIdRequest.transaction_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
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
  serialized_start=692,
  serialized_end=754,
)


_CLIENTBLOCKGETBYBATCHIDREQUEST = _descriptor.Descriptor(
  name='ClientBlockGetByBatchIdRequest',
  full_name='ClientBlockGetByBatchIdRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='batch_id', full_name='ClientBlockGetByBatchIdRequest.batch_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
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
  serialized_start=756,
  serialized_end=806,
)


_CLIENTBLOCKGETRESPONSE = _descriptor.Descriptor(
  name='ClientBlockGetResponse',
  full_name='ClientBlockGetResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='ClientBlockGetResponse.status', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='block', full_name='ClientBlockGetResponse.block', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _CLIENTBLOCKGETRESPONSE_STATUS,
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=809,
  serialized_end=993,
)

_CLIENTBLOCKLISTREQUEST.fields_by_name['paging'].message_type = sawtooth__settings_dot_protobuf_dot_client__list__control__pb2._CLIENTPAGINGCONTROLS
_CLIENTBLOCKLISTREQUEST.fields_by_name['sorting'].message_type = sawtooth__settings_dot_protobuf_dot_client__list__control__pb2._CLIENTSORTCONTROLS
_CLIENTBLOCKLISTRESPONSE.fields_by_name['status'].enum_type = _CLIENTBLOCKLISTRESPONSE_STATUS
_CLIENTBLOCKLISTRESPONSE.fields_by_name['blocks'].message_type = sawtooth__settings_dot_protobuf_dot_block__pb2._BLOCK
_CLIENTBLOCKLISTRESPONSE.fields_by_name['paging'].message_type = sawtooth__settings_dot_protobuf_dot_client__list__control__pb2._CLIENTPAGINGRESPONSE
_CLIENTBLOCKLISTRESPONSE_STATUS.containing_type = _CLIENTBLOCKLISTRESPONSE
_CLIENTBLOCKGETRESPONSE.fields_by_name['status'].enum_type = _CLIENTBLOCKGETRESPONSE_STATUS
_CLIENTBLOCKGETRESPONSE.fields_by_name['block'].message_type = sawtooth__settings_dot_protobuf_dot_block__pb2._BLOCK
_CLIENTBLOCKGETRESPONSE_STATUS.containing_type = _CLIENTBLOCKGETRESPONSE
DESCRIPTOR.message_types_by_name['ClientBlockListRequest'] = _CLIENTBLOCKLISTREQUEST
DESCRIPTOR.message_types_by_name['ClientBlockListResponse'] = _CLIENTBLOCKLISTRESPONSE
DESCRIPTOR.message_types_by_name['ClientBlockGetByIdRequest'] = _CLIENTBLOCKGETBYIDREQUEST
DESCRIPTOR.message_types_by_name['ClientBlockGetByNumRequest'] = _CLIENTBLOCKGETBYNUMREQUEST
DESCRIPTOR.message_types_by_name['ClientBlockGetByTransactionIdRequest'] = _CLIENTBLOCKGETBYTRANSACTIONIDREQUEST
DESCRIPTOR.message_types_by_name['ClientBlockGetByBatchIdRequest'] = _CLIENTBLOCKGETBYBATCHIDREQUEST
DESCRIPTOR.message_types_by_name['ClientBlockGetResponse'] = _CLIENTBLOCKGETRESPONSE

ClientBlockListRequest = _reflection.GeneratedProtocolMessageType('ClientBlockListRequest', (_message.Message,), dict(
  DESCRIPTOR = _CLIENTBLOCKLISTREQUEST,
  __module__ = 'sawtooth_settings.protobuf.client_block_pb2'
  # @@protoc_insertion_point(class_scope:ClientBlockListRequest)
  ))
_sym_db.RegisterMessage(ClientBlockListRequest)

ClientBlockListResponse = _reflection.GeneratedProtocolMessageType('ClientBlockListResponse', (_message.Message,), dict(
  DESCRIPTOR = _CLIENTBLOCKLISTRESPONSE,
  __module__ = 'sawtooth_settings.protobuf.client_block_pb2'
  # @@protoc_insertion_point(class_scope:ClientBlockListResponse)
  ))
_sym_db.RegisterMessage(ClientBlockListResponse)

ClientBlockGetByIdRequest = _reflection.GeneratedProtocolMessageType('ClientBlockGetByIdRequest', (_message.Message,), dict(
  DESCRIPTOR = _CLIENTBLOCKGETBYIDREQUEST,
  __module__ = 'sawtooth_settings.protobuf.client_block_pb2'
  # @@protoc_insertion_point(class_scope:ClientBlockGetByIdRequest)
  ))
_sym_db.RegisterMessage(ClientBlockGetByIdRequest)

ClientBlockGetByNumRequest = _reflection.GeneratedProtocolMessageType('ClientBlockGetByNumRequest', (_message.Message,), dict(
  DESCRIPTOR = _CLIENTBLOCKGETBYNUMREQUEST,
  __module__ = 'sawtooth_settings.protobuf.client_block_pb2'
  # @@protoc_insertion_point(class_scope:ClientBlockGetByNumRequest)
  ))
_sym_db.RegisterMessage(ClientBlockGetByNumRequest)

ClientBlockGetByTransactionIdRequest = _reflection.GeneratedProtocolMessageType('ClientBlockGetByTransactionIdRequest', (_message.Message,), dict(
  DESCRIPTOR = _CLIENTBLOCKGETBYTRANSACTIONIDREQUEST,
  __module__ = 'sawtooth_settings.protobuf.client_block_pb2'
  # @@protoc_insertion_point(class_scope:ClientBlockGetByTransactionIdRequest)
  ))
_sym_db.RegisterMessage(ClientBlockGetByTransactionIdRequest)

ClientBlockGetByBatchIdRequest = _reflection.GeneratedProtocolMessageType('ClientBlockGetByBatchIdRequest', (_message.Message,), dict(
  DESCRIPTOR = _CLIENTBLOCKGETBYBATCHIDREQUEST,
  __module__ = 'sawtooth_settings.protobuf.client_block_pb2'
  # @@protoc_insertion_point(class_scope:ClientBlockGetByBatchIdRequest)
  ))
_sym_db.RegisterMessage(ClientBlockGetByBatchIdRequest)

ClientBlockGetResponse = _reflection.GeneratedProtocolMessageType('ClientBlockGetResponse', (_message.Message,), dict(
  DESCRIPTOR = _CLIENTBLOCKGETRESPONSE,
  __module__ = 'sawtooth_settings.protobuf.client_block_pb2'
  # @@protoc_insertion_point(class_scope:ClientBlockGetResponse)
  ))
_sym_db.RegisterMessage(ClientBlockGetResponse)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n\025sawtooth.sdk.protobufP\001Z\020client_block_pb2'))
# @@protoc_insertion_point(module_scope)
