# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: protos/id_card.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='protos/id_card.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x14protos/id_card.proto\"1\n\nOcrRequest\x12\x11\n\tfront_img\x18\x01 \x01(\t\x12\x10\n\x08\x62\x61\x63k_img\x18\x02 \x01(\t\"K\n\x07OcrData\x12\x0c\n\x04type\x18\x01 \x01(\t\x12\x19\n\x05\x66ront\x18\x02 \x01(\x0b\x32\n.FrontData\x12\x17\n\x04\x62\x61\x63k\x18\x03 \x01(\x0b\x32\t.BackData\"%\n\x04Meta\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x05\x12\x0f\n\x07message\x18\x02 \x01(\t\":\n\x0bOcrResponse\x12\x13\n\x04meta\x18\x01 \x01(\x0b\x32\x05.Meta\x12\x16\n\x04\x64\x61ta\x18\x02 \x01(\x0b\x32\x08.OcrData\"\x1f\n\tFrontData\x12\x12\n\ncmt_number\x18\x01 \x01(\t\"&\n\x08\x42\x61\x63kData\x12\x1a\n\x12\x63mt_identification\x18\x01 \x01(\t23\n\tIDcardOcr\x12&\n\x0b\x65xtractText\x12\x0b.OcrRequest\x1a\x08.OcrData\"\x00\x62\x06proto3'
)




_OCRREQUEST = _descriptor.Descriptor(
  name='OcrRequest',
  full_name='OcrRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='front_img', full_name='OcrRequest.front_img', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='back_img', full_name='OcrRequest.back_img', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=24,
  serialized_end=73,
)


_OCRDATA = _descriptor.Descriptor(
  name='OcrData',
  full_name='OcrData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='OcrData.type', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='front', full_name='OcrData.front', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='back', full_name='OcrData.back', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=75,
  serialized_end=150,
)


_META = _descriptor.Descriptor(
  name='Meta',
  full_name='Meta',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='Meta.code', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='message', full_name='Meta.message', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=152,
  serialized_end=189,
)


_OCRRESPONSE = _descriptor.Descriptor(
  name='OcrResponse',
  full_name='OcrResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='meta', full_name='OcrResponse.meta', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='data', full_name='OcrResponse.data', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=191,
  serialized_end=249,
)


_FRONTDATA = _descriptor.Descriptor(
  name='FrontData',
  full_name='FrontData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='cmt_number', full_name='FrontData.cmt_number', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=251,
  serialized_end=282,
)


_BACKDATA = _descriptor.Descriptor(
  name='BackData',
  full_name='BackData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='cmt_identification', full_name='BackData.cmt_identification', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=284,
  serialized_end=322,
)

_OCRDATA.fields_by_name['front'].message_type = _FRONTDATA
_OCRDATA.fields_by_name['back'].message_type = _BACKDATA
_OCRRESPONSE.fields_by_name['meta'].message_type = _META
_OCRRESPONSE.fields_by_name['data'].message_type = _OCRDATA
DESCRIPTOR.message_types_by_name['OcrRequest'] = _OCRREQUEST
DESCRIPTOR.message_types_by_name['OcrData'] = _OCRDATA
DESCRIPTOR.message_types_by_name['Meta'] = _META
DESCRIPTOR.message_types_by_name['OcrResponse'] = _OCRRESPONSE
DESCRIPTOR.message_types_by_name['FrontData'] = _FRONTDATA
DESCRIPTOR.message_types_by_name['BackData'] = _BACKDATA
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

OcrRequest = _reflection.GeneratedProtocolMessageType('OcrRequest', (_message.Message,), {
  'DESCRIPTOR' : _OCRREQUEST,
  '__module__' : 'protos.id_card_pb2'
  # @@protoc_insertion_point(class_scope:OcrRequest)
  })
_sym_db.RegisterMessage(OcrRequest)

OcrData = _reflection.GeneratedProtocolMessageType('OcrData', (_message.Message,), {
  'DESCRIPTOR' : _OCRDATA,
  '__module__' : 'protos.id_card_pb2'
  # @@protoc_insertion_point(class_scope:OcrData)
  })
_sym_db.RegisterMessage(OcrData)

Meta = _reflection.GeneratedProtocolMessageType('Meta', (_message.Message,), {
  'DESCRIPTOR' : _META,
  '__module__' : 'protos.id_card_pb2'
  # @@protoc_insertion_point(class_scope:Meta)
  })
_sym_db.RegisterMessage(Meta)

OcrResponse = _reflection.GeneratedProtocolMessageType('OcrResponse', (_message.Message,), {
  'DESCRIPTOR' : _OCRRESPONSE,
  '__module__' : 'protos.id_card_pb2'
  # @@protoc_insertion_point(class_scope:OcrResponse)
  })
_sym_db.RegisterMessage(OcrResponse)

FrontData = _reflection.GeneratedProtocolMessageType('FrontData', (_message.Message,), {
  'DESCRIPTOR' : _FRONTDATA,
  '__module__' : 'protos.id_card_pb2'
  # @@protoc_insertion_point(class_scope:FrontData)
  })
_sym_db.RegisterMessage(FrontData)

BackData = _reflection.GeneratedProtocolMessageType('BackData', (_message.Message,), {
  'DESCRIPTOR' : _BACKDATA,
  '__module__' : 'protos.id_card_pb2'
  # @@protoc_insertion_point(class_scope:BackData)
  })
_sym_db.RegisterMessage(BackData)



_IDCARDOCR = _descriptor.ServiceDescriptor(
  name='IDcardOcr',
  full_name='IDcardOcr',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=324,
  serialized_end=375,
  methods=[
  _descriptor.MethodDescriptor(
    name='extractText',
    full_name='IDcardOcr.extractText',
    index=0,
    containing_service=None,
    input_type=_OCRREQUEST,
    output_type=_OCRDATA,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_IDCARDOCR)

DESCRIPTOR.services_by_name['IDcardOcr'] = _IDCARDOCR

# @@protoc_insertion_point(module_scope)
