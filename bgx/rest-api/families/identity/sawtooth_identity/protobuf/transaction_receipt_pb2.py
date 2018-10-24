# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: sawtooth_identity/protobuf/transaction_receipt.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from sawtooth_identity.protobuf import events_pb2 as sawtooth__identity_dot_protobuf_dot_events__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='sawtooth_identity/protobuf/transaction_receipt.proto',
  package='',
  syntax='proto3',
  serialized_pb=_b('\n4sawtooth_identity/protobuf/transaction_receipt.proto\x1a\'sawtooth_identity/protobuf/events.proto\"w\n\x12TransactionReceipt\x12#\n\rstate_changes\x18\x01 \x03(\x0b\x32\x0c.StateChange\x12\x16\n\x06\x65vents\x18\x02 \x03(\x0b\x32\x06.Event\x12\x0c\n\x04\x64\x61ta\x18\x03 \x03(\x0c\x12\x16\n\x0etransaction_id\x18\x04 \x01(\t\"{\n\x0bStateChange\x12\x0f\n\x07\x61\x64\x64ress\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x0c\x12\x1f\n\x04type\x18\x03 \x01(\x0e\x32\x11.StateChange.Type\"+\n\x04Type\x12\x0e\n\nTYPE_UNSET\x10\x00\x12\x07\n\x03SET\x10\x01\x12\n\n\x06\x44\x45LETE\x10\x02\"6\n\x0fStateChangeList\x12#\n\rstate_changes\x18\x01 \x03(\x0b\x32\x0c.StateChangeB*\n\x15sawtooth.sdk.protobufP\x01Z\x0ftxn_receipt_pb2b\x06proto3')
  ,
  dependencies=[sawtooth__identity_dot_protobuf_dot_events__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)



_STATECHANGE_TYPE = _descriptor.EnumDescriptor(
  name='Type',
  full_name='StateChange.Type',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='TYPE_UNSET', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SET', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DELETE', index=2, number=2,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=298,
  serialized_end=341,
)
_sym_db.RegisterEnumDescriptor(_STATECHANGE_TYPE)


_TRANSACTIONRECEIPT = _descriptor.Descriptor(
  name='TransactionReceipt',
  full_name='TransactionReceipt',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='state_changes', full_name='TransactionReceipt.state_changes', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='events', full_name='TransactionReceipt.events', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='data', full_name='TransactionReceipt.data', index=2,
      number=3, type=12, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='transaction_id', full_name='TransactionReceipt.transaction_id', index=3,
      number=4, type=9, cpp_type=9, label=1,
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
  serialized_start=97,
  serialized_end=216,
)


_STATECHANGE = _descriptor.Descriptor(
  name='StateChange',
  full_name='StateChange',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='address', full_name='StateChange.address', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='value', full_name='StateChange.value', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='type', full_name='StateChange.type', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _STATECHANGE_TYPE,
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=218,
  serialized_end=341,
)


_STATECHANGELIST = _descriptor.Descriptor(
  name='StateChangeList',
  full_name='StateChangeList',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='state_changes', full_name='StateChangeList.state_changes', index=0,
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
  serialized_start=343,
  serialized_end=397,
)

_TRANSACTIONRECEIPT.fields_by_name['state_changes'].message_type = _STATECHANGE
_TRANSACTIONRECEIPT.fields_by_name['events'].message_type = sawtooth__identity_dot_protobuf_dot_events__pb2._EVENT
_STATECHANGE.fields_by_name['type'].enum_type = _STATECHANGE_TYPE
_STATECHANGE_TYPE.containing_type = _STATECHANGE
_STATECHANGELIST.fields_by_name['state_changes'].message_type = _STATECHANGE
DESCRIPTOR.message_types_by_name['TransactionReceipt'] = _TRANSACTIONRECEIPT
DESCRIPTOR.message_types_by_name['StateChange'] = _STATECHANGE
DESCRIPTOR.message_types_by_name['StateChangeList'] = _STATECHANGELIST

TransactionReceipt = _reflection.GeneratedProtocolMessageType('TransactionReceipt', (_message.Message,), dict(
  DESCRIPTOR = _TRANSACTIONRECEIPT,
  __module__ = 'sawtooth_identity.protobuf.transaction_receipt_pb2'
  # @@protoc_insertion_point(class_scope:TransactionReceipt)
  ))
_sym_db.RegisterMessage(TransactionReceipt)

StateChange = _reflection.GeneratedProtocolMessageType('StateChange', (_message.Message,), dict(
  DESCRIPTOR = _STATECHANGE,
  __module__ = 'sawtooth_identity.protobuf.transaction_receipt_pb2'
  # @@protoc_insertion_point(class_scope:StateChange)
  ))
_sym_db.RegisterMessage(StateChange)

StateChangeList = _reflection.GeneratedProtocolMessageType('StateChangeList', (_message.Message,), dict(
  DESCRIPTOR = _STATECHANGELIST,
  __module__ = 'sawtooth_identity.protobuf.transaction_receipt_pb2'
  # @@protoc_insertion_point(class_scope:StateChangeList)
  ))
_sym_db.RegisterMessage(StateChangeList)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n\025sawtooth.sdk.protobufP\001Z\017txn_receipt_pb2'))
# @@protoc_insertion_point(module_scope)
