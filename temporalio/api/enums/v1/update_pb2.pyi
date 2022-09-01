"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
The MIT License

Copyright (c) 2020 Temporal Technologies Inc.  All rights reserved.

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
"""
import builtins
import google.protobuf.descriptor
import google.protobuf.internal.enum_type_wrapper
import sys
import typing

if sys.version_info >= (3, 10):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class _WorkflowUpdateResultAccessStyle:
    ValueType = typing.NewType("ValueType", builtins.int)
    V: typing_extensions.TypeAlias = ValueType

class _WorkflowUpdateResultAccessStyleEnumTypeWrapper(
    google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[
        _WorkflowUpdateResultAccessStyle.ValueType
    ],
    builtins.type,
):  # noqa: F821
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
    WORKFLOW_UPDATE_RESULT_ACCESS_STYLE_UNSPECIFIED: _WorkflowUpdateResultAccessStyle.ValueType  # 0
    WORKFLOW_UPDATE_RESULT_ACCESS_STYLE_REQUIRE_INLINE: _WorkflowUpdateResultAccessStyle.ValueType  # 1
    """Indicates that the update response _must_ be included as part of the gRPC
    response body
    """

class WorkflowUpdateResultAccessStyle(
    _WorkflowUpdateResultAccessStyle,
    metaclass=_WorkflowUpdateResultAccessStyleEnumTypeWrapper,
): ...

WORKFLOW_UPDATE_RESULT_ACCESS_STYLE_UNSPECIFIED: WorkflowUpdateResultAccessStyle.ValueType  # 0
WORKFLOW_UPDATE_RESULT_ACCESS_STYLE_REQUIRE_INLINE: WorkflowUpdateResultAccessStyle.ValueType  # 1
"""Indicates that the update response _must_ be included as part of the gRPC
response body
"""
global___WorkflowUpdateResultAccessStyle = WorkflowUpdateResultAccessStyle

class _WorkflowUpdateDurabilityPreference:
    ValueType = typing.NewType("ValueType", builtins.int)
    V: typing_extensions.TypeAlias = ValueType

class _WorkflowUpdateDurabilityPreferenceEnumTypeWrapper(
    google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[
        _WorkflowUpdateDurabilityPreference.ValueType
    ],
    builtins.type,
):  # noqa: F821
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
    WORKFLOW_UPDATE_DURABILITY_PREFERENCE_UNSPECIFIED: _WorkflowUpdateDurabilityPreference.ValueType  # 0
    """The workflow expresses no preference as to the durability of the
    the associated update.
    """
    WORKFLOW_UPDATE_DURABILITY_PREFERENCE_BYPASS: _WorkflowUpdateDurabilityPreference.ValueType  # 1
    """Used by a workflow to indicate that no workflow state mutation occurred
    while processing the update and that it wishes that the update not be
    made durable (and thus not take up space in workflow history).
    """

class WorkflowUpdateDurabilityPreference(
    _WorkflowUpdateDurabilityPreference,
    metaclass=_WorkflowUpdateDurabilityPreferenceEnumTypeWrapper,
): ...

WORKFLOW_UPDATE_DURABILITY_PREFERENCE_UNSPECIFIED: WorkflowUpdateDurabilityPreference.ValueType  # 0
"""The workflow expresses no preference as to the durability of the
the associated update.
"""
WORKFLOW_UPDATE_DURABILITY_PREFERENCE_BYPASS: WorkflowUpdateDurabilityPreference.ValueType  # 1
"""Used by a workflow to indicate that no workflow state mutation occurred
while processing the update and that it wishes that the update not be
made durable (and thus not take up space in workflow history).
"""
global___WorkflowUpdateDurabilityPreference = WorkflowUpdateDurabilityPreference
