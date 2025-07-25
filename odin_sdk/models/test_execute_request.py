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
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class TestExecuteRequest(BaseModel):
    """
    Request model for test execution without database persistence
    """ # noqa: E501
    runtime: Optional[Any] = Field(description="Runtime version (e.g., 'python3.11', 'nodejs20.x')")
    script: Optional[Any] = Field(description="Script code to execute")
    entry_point: Optional[Any] = Field(default=None, description="Entry point function name")
    dependencies: Optional[Any] = Field(default=None, description="List of package dependencies")
    args: Optional[Any] = Field(default=None, description="Positional arguments")
    kwargs: Optional[Any] = Field(default=None, description="Keyword arguments")
    __properties: ClassVar[List[str]] = ["runtime", "script", "entry_point", "dependencies", "args", "kwargs"]

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
        """Create an instance of TestExecuteRequest from a JSON string"""
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
        # set to None if runtime (nullable) is None
        # and model_fields_set contains the field
        if self.runtime is None and "runtime" in self.model_fields_set:
            _dict['runtime'] = None

        # set to None if script (nullable) is None
        # and model_fields_set contains the field
        if self.script is None and "script" in self.model_fields_set:
            _dict['script'] = None

        # set to None if entry_point (nullable) is None
        # and model_fields_set contains the field
        if self.entry_point is None and "entry_point" in self.model_fields_set:
            _dict['entry_point'] = None

        # set to None if dependencies (nullable) is None
        # and model_fields_set contains the field
        if self.dependencies is None and "dependencies" in self.model_fields_set:
            _dict['dependencies'] = None

        # set to None if args (nullable) is None
        # and model_fields_set contains the field
        if self.args is None and "args" in self.model_fields_set:
            _dict['args'] = None

        # set to None if kwargs (nullable) is None
        # and model_fields_set contains the field
        if self.kwargs is None and "kwargs" in self.model_fields_set:
            _dict['kwargs'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of TestExecuteRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "runtime": obj.get("runtime"),
            "script": obj.get("script"),
            "entry_point": obj.get("entry_point"),
            "dependencies": obj.get("dependencies"),
            "args": obj.get("args"),
            "kwargs": obj.get("kwargs")
        })
        return _obj


