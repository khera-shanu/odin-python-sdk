# coding: utf-8

"""
    API Docs

    API Documentation to interact with

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Any, ClassVar, Dict, List, Optional
from pydantic import BaseModel
from odin_sdk.models.computation_id import ComputationId
from odin_sdk.models.history_table import HistoryTable
from odin_sdk.models.task_id import TaskId
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class ComputeAllRowsResponse(BaseModel):
    """
    ComputeAllRowsResponse
    """ # noqa: E501
    message: Optional[Any]
    total_rows_processed: Optional[Any]
    total_columns_updated: Optional[Any]
    updated_columns: Optional[Any]
    failed_rows: Optional[Any]
    stopped_due_to_failures: Optional[Any]
    retry_attempts: Optional[Any]
    computation_id: Optional[ComputationId] = None
    history_table: Optional[HistoryTable] = None
    task_id: Optional[TaskId] = None
    __properties: ClassVar[List[str]] = ["message", "total_rows_processed", "total_columns_updated", "updated_columns", "failed_rows", "stopped_due_to_failures", "retry_attempts", "computation_id", "history_table", "task_id"]

    model_config = {
        "populate_by_name": True,
        "validate_assignment": True,
        "protected_namespaces": (),
    }


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of ComputeAllRowsResponse from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        _dict = self.model_dump(
            by_alias=True,
            exclude={
            },
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of computation_id
        if self.computation_id:
            _dict['computation_id'] = self.computation_id.to_dict()
        # override the default output from pydantic by calling `to_dict()` of history_table
        if self.history_table:
            _dict['history_table'] = self.history_table.to_dict()
        # override the default output from pydantic by calling `to_dict()` of task_id
        if self.task_id:
            _dict['task_id'] = self.task_id.to_dict()
        # set to None if message (nullable) is None
        # and model_fields_set contains the field
        if self.message is None and "message" in self.model_fields_set:
            _dict['message'] = None

        # set to None if total_rows_processed (nullable) is None
        # and model_fields_set contains the field
        if self.total_rows_processed is None and "total_rows_processed" in self.model_fields_set:
            _dict['total_rows_processed'] = None

        # set to None if total_columns_updated (nullable) is None
        # and model_fields_set contains the field
        if self.total_columns_updated is None and "total_columns_updated" in self.model_fields_set:
            _dict['total_columns_updated'] = None

        # set to None if updated_columns (nullable) is None
        # and model_fields_set contains the field
        if self.updated_columns is None and "updated_columns" in self.model_fields_set:
            _dict['updated_columns'] = None

        # set to None if failed_rows (nullable) is None
        # and model_fields_set contains the field
        if self.failed_rows is None and "failed_rows" in self.model_fields_set:
            _dict['failed_rows'] = None

        # set to None if stopped_due_to_failures (nullable) is None
        # and model_fields_set contains the field
        if self.stopped_due_to_failures is None and "stopped_due_to_failures" in self.model_fields_set:
            _dict['stopped_due_to_failures'] = None

        # set to None if retry_attempts (nullable) is None
        # and model_fields_set contains the field
        if self.retry_attempts is None and "retry_attempts" in self.model_fields_set:
            _dict['retry_attempts'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of ComputeAllRowsResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "message": obj.get("message"),
            "total_rows_processed": obj.get("total_rows_processed"),
            "total_columns_updated": obj.get("total_columns_updated"),
            "updated_columns": obj.get("updated_columns"),
            "failed_rows": obj.get("failed_rows"),
            "stopped_due_to_failures": obj.get("stopped_due_to_failures"),
            "computation_id": ComputationId.from_dict(obj.get("computation_id")) if obj.get("computation_id") is not None else None,
            "history_table": HistoryTable.from_dict(obj.get("history_table")) if obj.get("history_table") is not None else None,
            "task_id": TaskId.from_dict(obj.get("task_id")) if obj.get("task_id") is not None else None
        })
        return _obj


