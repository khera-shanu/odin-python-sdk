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
from pydantic import Field
from odin_sdk.models.change_log1 import ChangeLog1
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class PublishToolRequest(BaseModel):
    """
    PublishToolRequest
    """ # noqa: E501
    version_type: Optional[Any] = Field(default=None, description="Version increment type: major, minor, or patch")
    change_log: Optional[ChangeLog1] = None
    __properties: ClassVar[List[str]] = ["version_type", "change_log"]

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
        """Create an instance of PublishToolRequest from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of change_log
        if self.change_log:
            _dict['change_log'] = self.change_log.to_dict()
        # set to None if version_type (nullable) is None
        # and model_fields_set contains the field
        if self.version_type is None and "version_type" in self.model_fields_set:
            _dict['version_type'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of PublishToolRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "version_type": obj.get("version_type"),
            "change_log": ChangeLog1.from_dict(obj.get("change_log")) if obj.get("change_log") is not None else None
        })
        return _obj


