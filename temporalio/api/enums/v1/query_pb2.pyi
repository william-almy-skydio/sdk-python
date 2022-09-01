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

class _QueryResultType:
    ValueType = typing.NewType("ValueType", builtins.int)
    V: typing_extensions.TypeAlias = ValueType

class _QueryResultTypeEnumTypeWrapper(
    google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[
        _QueryResultType.ValueType
    ],
    builtins.type,
):  # noqa: F821
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
    QUERY_RESULT_TYPE_UNSPECIFIED: _QueryResultType.ValueType  # 0
    QUERY_RESULT_TYPE_ANSWERED: _QueryResultType.ValueType  # 1
    QUERY_RESULT_TYPE_FAILED: _QueryResultType.ValueType  # 2

class QueryResultType(_QueryResultType, metaclass=_QueryResultTypeEnumTypeWrapper): ...

QUERY_RESULT_TYPE_UNSPECIFIED: QueryResultType.ValueType  # 0
QUERY_RESULT_TYPE_ANSWERED: QueryResultType.ValueType  # 1
QUERY_RESULT_TYPE_FAILED: QueryResultType.ValueType  # 2
global___QueryResultType = QueryResultType

class _QueryRejectCondition:
    ValueType = typing.NewType("ValueType", builtins.int)
    V: typing_extensions.TypeAlias = ValueType

class _QueryRejectConditionEnumTypeWrapper(
    google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[
        _QueryRejectCondition.ValueType
    ],
    builtins.type,
):  # noqa: F821
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
    QUERY_REJECT_CONDITION_UNSPECIFIED: _QueryRejectCondition.ValueType  # 0
    QUERY_REJECT_CONDITION_NONE: _QueryRejectCondition.ValueType  # 1
    """None indicates that query should not be rejected."""
    QUERY_REJECT_CONDITION_NOT_OPEN: _QueryRejectCondition.ValueType  # 2
    """NotOpen indicates that query should be rejected if workflow is not open."""
    QUERY_REJECT_CONDITION_NOT_COMPLETED_CLEANLY: _QueryRejectCondition.ValueType  # 3
    """NotCompletedCleanly indicates that query should be rejected if workflow did not complete cleanly."""

class QueryRejectCondition(
    _QueryRejectCondition, metaclass=_QueryRejectConditionEnumTypeWrapper
): ...

QUERY_REJECT_CONDITION_UNSPECIFIED: QueryRejectCondition.ValueType  # 0
QUERY_REJECT_CONDITION_NONE: QueryRejectCondition.ValueType  # 1
"""None indicates that query should not be rejected."""
QUERY_REJECT_CONDITION_NOT_OPEN: QueryRejectCondition.ValueType  # 2
"""NotOpen indicates that query should be rejected if workflow is not open."""
QUERY_REJECT_CONDITION_NOT_COMPLETED_CLEANLY: QueryRejectCondition.ValueType  # 3
"""NotCompletedCleanly indicates that query should be rejected if workflow did not complete cleanly."""
global___QueryRejectCondition = QueryRejectCondition
