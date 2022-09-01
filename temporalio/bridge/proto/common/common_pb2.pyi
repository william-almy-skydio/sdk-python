"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.protobuf.descriptor
import google.protobuf.message
import sys

if sys.version_info >= (3, 8):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class NamespacedWorkflowExecution(google.protobuf.message.Message):
    """Identifying information about a particular workflow execution, including namespace"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    NAMESPACE_FIELD_NUMBER: builtins.int
    WORKFLOW_ID_FIELD_NUMBER: builtins.int
    RUN_ID_FIELD_NUMBER: builtins.int
    namespace: builtins.str
    """Namespace the workflow run is located in"""
    workflow_id: builtins.str
    """Can never be empty"""
    run_id: builtins.str
    """May be empty if the most recent run of the workflow with the given ID is being targeted"""
    def __init__(
        self,
        *,
        namespace: builtins.str = ...,
        workflow_id: builtins.str = ...,
        run_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal[
            "namespace",
            b"namespace",
            "run_id",
            b"run_id",
            "workflow_id",
            b"workflow_id",
        ],
    ) -> None: ...

global___NamespacedWorkflowExecution = NamespacedWorkflowExecution
