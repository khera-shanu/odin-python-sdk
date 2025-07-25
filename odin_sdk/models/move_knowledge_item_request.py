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
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class MoveKnowledgeItemRequest(BaseModel):
    """
    MoveKnowledgeItemRequest
    """ # noqa: E501
    project_id: Optional[Any]
    source: Optional[Any]
    destination_path: Optional[Any]
    is_folder: Optional[Any] = None
    __properties: ClassVar[List[str]] = ["project_id", "source", "destination_path", "is_folder"]

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
        """Create an instance of MoveKnowledgeItemRequest from a JSON string"""
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
        # set to None if project_id (nullable) is None
        # and model_fields_set contains the field
        if self.project_id is None and "project_id" in self.model_fields_set:
            _dict['project_id'] = None

        # set to None if source (nullable) is None
        # and model_fields_set contains the field
        if self.source is None and "source" in self.model_fields_set:
            _dict['source'] = None

        # set to None if destination_path (nullable) is None
        # and model_fields_set contains the field
        if self.destination_path is None and "destination_path" in self.model_fields_set:
            _dict['destination_path'] = None

        # set to None if is_folder (nullable) is None
        # and model_fields_set contains the field
        if self.is_folder is None and "is_folder" in self.model_fields_set:
            _dict['is_folder'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of MoveKnowledgeItemRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "project_id": obj.get("project_id"),
            "source": obj.get("source"),
            "destination_path": obj.get("destination_path"),
            "is_folder": obj.get("is_folder")
        })
        return _obj


