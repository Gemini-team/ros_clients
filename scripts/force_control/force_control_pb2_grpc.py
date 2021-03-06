# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import force_control_pb2 as force__control__pb2


class ForceControlStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.ApplyForce = channel.unary_unary(
                '/gemini.forcecontrol.ForceControl/ApplyForce',
                request_serializer=force__control__pb2.ForceRequest.SerializeToString,
                response_deserializer=force__control__pb2.ForceResponse.FromString,
                )


class ForceControlServicer(object):
    """Missing associated documentation comment in .proto file."""

    def ApplyForce(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ForceControlServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'ApplyForce': grpc.unary_unary_rpc_method_handler(
                    servicer.ApplyForce,
                    request_deserializer=force__control__pb2.ForceRequest.FromString,
                    response_serializer=force__control__pb2.ForceResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'gemini.forcecontrol.ForceControl', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class ForceControl(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def ApplyForce(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/gemini.forcecontrol.ForceControl/ApplyForce',
            force__control__pb2.ForceRequest.SerializeToString,
            force__control__pb2.ForceResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
