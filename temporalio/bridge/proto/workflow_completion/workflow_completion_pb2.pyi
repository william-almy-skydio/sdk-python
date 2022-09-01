"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import collections.abc
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.message
import sys
import temporalio.api.failure.v1.message_pb2
import temporalio.bridge.proto.workflow_commands.workflow_commands_pb2

if sys.version_info >= (3, 8):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class WorkflowActivationCompletion(google.protobuf.message.Message):
    """/ Result of a single workflow activation, reported from lang to core"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    RUN_ID_FIELD_NUMBER: builtins.int
    SUCCESSFUL_FIELD_NUMBER: builtins.int
    FAILED_FIELD_NUMBER: builtins.int
    run_id: builtins.str
    """The run id from the workflow activation you are completing"""
    @property
    def successful(self) -> global___Success: ...
    @property
    def failed(self) -> global___Failure: ...
    def __init__(
        self,
        *,
        run_id: builtins.str = ...,
        successful: global___Success | None = ...,
        failed: global___Failure | None = ...,
    ) -> None: ...
    def HasField(
        self,
        field_name: typing_extensions.Literal[
            "failed", b"failed", "status", b"status", "successful", b"successful"
        ],
    ) -> builtins.bool: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal[
            "failed",
            b"failed",
            "run_id",
            b"run_id",
            "status",
            b"status",
            "successful",
            b"successful",
        ],
    ) -> None: ...
    def WhichOneof(
        self, oneof_group: typing_extensions.Literal["status", b"status"]
    ) -> typing_extensions.Literal["successful", "failed"] | None: ...

global___WorkflowActivationCompletion = WorkflowActivationCompletion

class Success(google.protobuf.message.Message):
    """/ Successful workflow activation with a list of commands generated by the workflow execution"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    COMMANDS_FIELD_NUMBER: builtins.int
    @property
    def commands(
        self,
    ) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[
        temporalio.bridge.proto.workflow_commands.workflow_commands_pb2.WorkflowCommand
    ]:
        """A list of commands to send back to the temporal server"""
    def __init__(
        self,
        *,
        commands: collections.abc.Iterable[
            temporalio.bridge.proto.workflow_commands.workflow_commands_pb2.WorkflowCommand
        ]
        | None = ...,
    ) -> None: ...
    def ClearField(
        self, field_name: typing_extensions.Literal["commands", b"commands"]
    ) -> None: ...

global___Success = Success

class Failure(google.protobuf.message.Message):
    """/ Failure to activate or execute a workflow"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    FAILURE_FIELD_NUMBER: builtins.int
    @property
    def failure(self) -> temporalio.api.failure.v1.message_pb2.Failure: ...
    def __init__(
        self,
        *,
        failure: temporalio.api.failure.v1.message_pb2.Failure | None = ...,
    ) -> None: ...
    def HasField(
        self, field_name: typing_extensions.Literal["failure", b"failure"]
    ) -> builtins.bool: ...
    def ClearField(
        self, field_name: typing_extensions.Literal["failure", b"failure"]
    ) -> None: ...

global___Failure = Failure
