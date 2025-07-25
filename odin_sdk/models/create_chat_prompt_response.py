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
from odin_sdk.models.custom_agent import CustomAgent
from odin_sdk.models.document_id import DocumentId
from odin_sdk.models.document_keys1 import DocumentKeys1
from odin_sdk.models.metadata1 import Metadata1
from odin_sdk.models.name import Name
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class CreateChatPromptResponse(BaseModel):
    """
    CreateChatPromptResponse
    """ # noqa: E501
    name: Optional[Name] = None
    chat_id: Optional[Any]
    metadata: Optional[Metadata1] = None
    document_keys: Optional[DocumentKeys1] = None
    document_id: Optional[DocumentId] = None
    created_at: Optional[Any]
    custom_agent: Optional[CustomAgent] = None
    __properties: ClassVar[List[str]] = ["name", "chat_id", "metadata", "document_keys", "document_id", "created_at", "custom_agent"]

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
        """Create an instance of CreateChatPromptResponse from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of metadata
        if self.metadata:
            _dict['metadata'] = self.metadata.to_dict()
        # override the default output from pydantic by calling `to_dict()` of document_keys
        if self.document_keys:
            _dict['document_keys'] = self.document_keys.to_dict()
        # override the default output from pydantic by calling `to_dict()` of document_id
        if self.document_id:
            _dict['document_id'] = self.document_id.to_dict()
        # override the default output from pydantic by calling `to_dict()` of custom_agent
        if self.custom_agent:
            _dict['custom_agent'] = self.custom_agent.to_dict()
        # set to None if chat_id (nullable) is None
        # and model_fields_set contains the field
        if self.chat_id is None and "chat_id" in self.model_fields_set:
            _dict['chat_id'] = None

        # set to None if created_at (nullable) is None
        # and model_fields_set contains the field
        if self.created_at is None and "created_at" in self.model_fields_set:
            _dict['created_at'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of CreateChatPromptResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "name": Name.from_dict(obj.get("name")) if obj.get("name") is not None else None,
            "chat_id": obj.get("chat_id"),
            "metadata": Metadata1.from_dict(obj.get("metadata")) if obj.get("metadata") is not None else None,
            "document_keys": DocumentKeys1.from_dict(obj.get("document_keys")) if obj.get("document_keys") is not None else None,
            "document_id": DocumentId.from_dict(obj.get("document_id")) if obj.get("document_id") is not None else None,
            "created_at": obj.get("created_at"),
            "custom_agent": CustomAgent.from_dict(obj.get("custom_agent")) if obj.get("custom_agent") is not None else None
        })
        return _obj


