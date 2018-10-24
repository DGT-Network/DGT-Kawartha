# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: sawtooth_settings/protobuf/batch.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from sawtooth_settings.protobuf import transaction_pb2 as sawtooth__settings_dot_protobuf_dot_transaction__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='sawtooth_settings/protobuf/batch.proto',
  package='',
  syntax='proto3',
  serialized_pb=_b('\n&sawtooth_settings/protobuf/batch.proto\x1a,sawtooth_settings/protobuf/transaction.proto\"A\n\x0b\x42\x61tchHeader\x12\x19\n\x11signer_public_key\x18\x01 \x01(\t\x12\x17\n\x0ftransaction_ids\x18\x02 \x03(\t\"d\n\x05\x42\x61tch\x12\x0e\n\x06header\x18\x01 \x01(\x0c\x12\x18\n\x10header_signature\x18\x02 \x01(\t\x12\"\n\x0ctransactions\x18\x03 \x03(\x0b\x32\x0c.Transaction\x12\r\n\x05trace\x18\x04 \x01(\x08\"$\n\tBatchList\x12\x17\n\x07\x62\x61tches\x18\x01 \x03(\x0b\x32\x06.BatchB$\n\x15sawtooth.sdk.protobufP\x01Z\tbatch_pb2b\x06proto3')
  ,
  dependencies=[sawtooth__settings_dot_protobuf_dot_transaction__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_BATCHHEADER = _descriptor.Descriptor(
  name='BatchHeader',
  full_name='BatchHeader',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='signer_public_key', full_name='BatchHeader.signer_public_key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='transaction_ids', full_name='BatchHeader.transaction_ids', index=1,
      number=2, type=9, cpp_type=9, label=3,
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
  serialized_start=88,
  serialized_end=153,
)


_BATCH = _descriptor.Descriptor(
  name='Batch',
  full_name='Batch',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='header', full_name='Batch.header', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='header_signature', full_name='Batch.header_signature', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='transactions', full_name='Batch.transactions', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='trace', full_name='Batch.trace', index=3,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
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
  serialized_start=155,
  serialized_end=255,
)


_BATCHLIST = _descriptor.Descriptor(
  name='BatchList',
  full_name='BatchList',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='batches', full_name='BatchList.batches', index=0,
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
  serialized_start=257,
  serialized_end=293,
)

_BATCH.fields_by_name['transactions'].message_type = sawtooth__settings_dot_protobuf_dot_transaction__pb2._TRANSACTION
_BATCHLIST.fields_by_name['batches'].message_type = _BATCH
DESCRIPTOR.message_types_by_name['BatchHeader'] = _BATCHHEADER
DESCRIPTOR.message_types_by_name['Batch'] = _BATCH
DESCRIPTOR.message_types_by_name['BatchList'] = _BATCHLIST

BatchHeader = _reflection.GeneratedProtocolMessageType('BatchHeader', (_message.Message,), dict(
  DESCRIPTOR = _BATCHHEADER,
  __module__ = 'sawtooth_settings.protobuf.batch_pb2'
  # @@protoc_insertion_point(class_scope:BatchHeader)
  ))
_sym_db.RegisterMessage(BatchHeader)

Batch = _reflection.GeneratedProtocolMessageType('Batch', (_message.Message,), dict(
  DESCRIPTOR = _BATCH,
  __module__ = 'sawtooth_settings.protobuf.batch_pb2'
  # @@protoc_insertion_point(class_scope:Batch)
  ))
_sym_db.RegisterMessage(Batch)

BatchList = _reflection.GeneratedProtocolMessageType('BatchList', (_message.Message,), dict(
  DESCRIPTOR = _BATCHLIST,
  __module__ = 'sawtooth_settings.protobuf.batch_pb2'
  # @@protoc_insertion_point(class_scope:BatchList)
  ))
_sym_db.RegisterMessage(BatchList)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n\025sawtooth.sdk.protobufP\001Z\tbatch_pb2'))
# @@protoc_insertion_point(module_scope)
