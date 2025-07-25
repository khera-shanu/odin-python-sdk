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
from odin_sdk.models.created_at1 import CreatedAt1
from odin_sdk.models.key import Key
from odin_sdk.models.size import Size
from odin_sdk.models.updated_at1 import UpdatedAt1
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class FileItem(BaseModel):
    """
    FileItem
    """ # noqa: E501
    name: Optional[Any]
    key: Key
    path: Optional[Any]
    size: Optional[Size] = None
    type: Optional[Any]
    created_at: Optional[CreatedAt1] = None
    updated_at: Optional[UpdatedAt1] = None
    __properties: ClassVar[List[str]] = ["name", "key", "path", "size", "type", "created_at", "updated_at"]

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
        """Create an instance of FileItem from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of key
        if self.key:
            _dict['key'] = self.key.to_dict()
        # override the default output from pydantic by calling `to_dict()` of size
        if self.size:
            _dict['size'] = self.size.to_dict()
        # override the default output from pydantic by calling `to_dict()` of created_at
        if self.created_at:
            _dict['created_at'] = self.created_at.to_dict()
        # override the default output from pydantic by calling `to_dict()` of updated_at
        if self.updated_at:
            _dict['updated_at'] = self.updated_at.to_dict()
        # set to None if name (nullable) is None
        # and model_fields_set contains the field
        if self.name is None and "name" in self.model_fields_set:
            _dict['name'] = None

        # set to None if path (nullable) is None
        # and model_fields_set contains the field
        if self.path is None and "path" in self.model_fields_set:
            _dict['path'] = None

        # set to None if type (nullable) is None
        # and model_fields_set contains the field
        if self.type is None and "type" in self.model_fields_set:
            _dict['type'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of FileItem from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "name": obj.get("name"),
            "key": Key.from_dict(obj.get("key")) if obj.get("key") is not None else None,
            "path": obj.get("path"),
            "size": Size.from_dict(obj.get("size")) if obj.get("size") is not None else None,
            "type": obj.get("type"),
            "created_at": CreatedAt1.from_dict(obj.get("created_at")) if obj.get("created_at") is not None else None,
            "updated_at": UpdatedAt1.from_dict(obj.get("updated_at")) if obj.get("updated_at") is not None else None
        })
        return _obj


