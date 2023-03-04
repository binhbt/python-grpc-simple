# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from protos import id_card_pb2 as protos_dot_id__card__pb2


class IDcardOcrStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.extractText = channel.unary_unary(
                '/IDcardOcr/extractText',
                request_serializer=protos_dot_id__card__pb2.OcrRequest.SerializeToString,
                response_deserializer=protos_dot_id__card__pb2.OcrData.FromString,
                )


class IDcardOcrServicer(object):
    """Missing associated documentation comment in .proto file."""

    def extractText(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_IDcardOcrServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'extractText': grpc.unary_unary_rpc_method_handler(
                    servicer.extractText,
                    request_deserializer=protos_dot_id__card__pb2.OcrRequest.FromString,
                    response_serializer=protos_dot_id__card__pb2.OcrData.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'IDcardOcr', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class IDcardOcr(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def extractText(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/IDcardOcr/extractText',
            protos_dot_id__card__pb2.OcrRequest.SerializeToString,
            protos_dot_id__card__pb2.OcrData.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)