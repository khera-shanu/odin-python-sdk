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
from odin_sdk.models.custom_resource_settings1 import CustomResourceSettings1
from odin_sdk.models.dependencies import Dependencies
from odin_sdk.models.description4 import Description4
from odin_sdk.models.entry_point import EntryPoint
from odin_sdk.models.name1 import Name1
from odin_sdk.models.runtime1 import Runtime1
from odin_sdk.models.script import Script
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class CodeScriptUpdate(BaseModel):
    """
    Request model for updating a code script
    """ # noqa: E501
    name: Optional[Name1] = None
    description: Optional[Description4] = None
    script: Optional[Script] = None
    runtime: Optional[Runtime1] = None
    entry_point: Optional[EntryPoint] = None
    dependencies: Optional[Dependencies] = None
    custom_resource_settings: Optional[CustomResourceSettings1] = None
    __properties: ClassVar[List[str]] = ["name", "description", "script", "runtime", "entry_point", "dependencies", "custom_resource_settings"]

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
        """Create an instance of CodeScriptUpdate from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of name
        if self.name:
            _dict['name'] = self.name.to_dict()
        # override the default output from pydantic by calling `to_dict()` of description
        if self.description:
            _dict['description'] = self.description.to_dict()
        # override the default output from pydantic by calling `to_dict()` of script
        if self.script:
            _dict['script'] = self.script.to_dict()
        # override the default output from pydantic by calling `to_dict()` of runtime
        if self.runtime:
            _dict['runtime'] = self.runtime.to_dict()
        # override the default output from pydantic by calling `to_dict()` of entry_point
        if self.entry_point:
            _dict['entry_point'] = self.entry_point.to_dict()
        # override the default output from pydantic by calling `to_dict()` of dependencies
        if self.dependencies:
            _dict['dependencies'] = self.dependencies.to_dict()
        # override the default output from pydantic by calling `to_dict()` of custom_resource_settings
        if self.custom_resource_settings:
            _dict['custom_resource_settings'] = self.custom_resource_settings.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of CodeScriptUpdate from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "name": Name1.from_dict(obj.get("name")) if obj.get("name") is not None else None,
            "description": Description4.from_dict(obj.get("description")) if obj.get("description") is not None else None,
            "script": Script.from_dict(obj.get("script")) if obj.get("script") is not None else None,
            "runtime": Runtime1.from_dict(obj.get("runtime")) if obj.get("runtime") is not None else None,
            "entry_point": EntryPoint.from_dict(obj.get("entry_point")) if obj.get("entry_point") is not None else None,
            "dependencies": Dependencies.from_dict(obj.get("dependencies")) if obj.get("dependencies") is not None else None,
            "custom_resource_settings": CustomResourceSettings1.from_dict(obj.get("custom_resource_settings")) if obj.get("custom_resource_settings") is not None else None
        })
        return _obj


