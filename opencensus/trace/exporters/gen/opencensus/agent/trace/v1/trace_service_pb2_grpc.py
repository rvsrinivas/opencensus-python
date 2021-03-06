# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from opencensus.trace.exporters.gen.opencensus.agent.trace.v1 import trace_service_pb2 as opencensus_dot_proto_dot_agent_dot_trace_dot_v1_dot_trace__service__pb2


class TraceServiceStub(object):
    # missing associated documentation comment in .proto file
    pass

    def __init__(self, channel):
        """Constructor.

        Args:
          channel: A grpc.Channel.
        """
        self.Config = channel.stream_stream(
            '/opencensus.proto.agent.trace.v1.TraceService/Config',
            request_serializer=opencensus_dot_proto_dot_agent_dot_trace_dot_v1_dot_trace__service__pb2.CurrentLibraryConfig.SerializeToString,
            response_deserializer=opencensus_dot_proto_dot_agent_dot_trace_dot_v1_dot_trace__service__pb2.UpdatedLibraryConfig.FromString,
        )
        self.Export = channel.stream_stream(
            '/opencensus.proto.agent.trace.v1.TraceService/Export',
            request_serializer=opencensus_dot_proto_dot_agent_dot_trace_dot_v1_dot_trace__service__pb2.ExportTraceServiceRequest.SerializeToString,
            response_deserializer=opencensus_dot_proto_dot_agent_dot_trace_dot_v1_dot_trace__service__pb2.ExportTraceServiceResponse.FromString,
        )


class TraceServiceServicer(object):
    # missing associated documentation comment in .proto file
    pass

    def Config(self, request_iterator, context):
        """After initialization, this RPC must be kept alive for the
        entire life of the application. The agent pushes configs
        down to applications via a stream.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Export(self, request_iterator, context):
        """Allows applications to send spans to the agent.
        For performance reasons, it is recommended to keep this RPC
        alive for the entire life of the application.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_TraceServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
        'Config': grpc.stream_stream_rpc_method_handler(
            servicer.Config,
            request_deserializer=opencensus_dot_proto_dot_agent_dot_trace_dot_v1_dot_trace__service__pb2.CurrentLibraryConfig.FromString,
            response_serializer=opencensus_dot_proto_dot_agent_dot_trace_dot_v1_dot_trace__service__pb2.UpdatedLibraryConfig.SerializeToString,
        ),
        'Export': grpc.stream_stream_rpc_method_handler(
            servicer.Export,
            request_deserializer=opencensus_dot_proto_dot_agent_dot_trace_dot_v1_dot_trace__service__pb2.ExportTraceServiceRequest.FromString,
            response_serializer=opencensus_dot_proto_dot_agent_dot_trace_dot_v1_dot_trace__service__pb2.ExportTraceServiceResponse.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        'opencensus.proto.agent.trace.v1.TraceService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
