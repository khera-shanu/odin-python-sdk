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
from odin_sdk.models.credits_used1 import CreditsUsed1
from odin_sdk.models.name import Name
from odin_sdk.models.subscription_status import SubscriptionStatus
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class UserResponse(BaseModel):
    """
    UserResponse
    """ # noqa: E501
    user_id: Optional[Any]
    email: Optional[Any]
    name: Name
    is_admin: Optional[Any] = None
    subscription_status: Optional[SubscriptionStatus] = None
    credits_used: Optional[CreditsUsed1] = None
    __properties: ClassVar[List[str]] = ["user_id", "email", "name", "is_admin", "subscription_status", "credits_used"]

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
        """Create an instance of UserResponse from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of subscription_status
        if self.subscription_status:
            _dict['subscription_status'] = self.subscription_status.to_dict()
        # override the default output from pydantic by calling `to_dict()` of credits_used
        if self.credits_used:
            _dict['credits_used'] = self.credits_used.to_dict()
        # set to None if user_id (nullable) is None
        # and model_fields_set contains the field
        if self.user_id is None and "user_id" in self.model_fields_set:
            _dict['user_id'] = None

        # set to None if email (nullable) is None
        # and model_fields_set contains the field
        if self.email is None and "email" in self.model_fields_set:
            _dict['email'] = None

        # set to None if is_admin (nullable) is None
        # and model_fields_set contains the field
        if self.is_admin is None and "is_admin" in self.model_fields_set:
            _dict['is_admin'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of UserResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "user_id": obj.get("user_id"),
            "email": obj.get("email"),
            "name": Name.from_dict(obj.get("name")) if obj.get("name") is not None else None,
            "is_admin": obj.get("is_admin"),
            "subscription_status": SubscriptionStatus.from_dict(obj.get("subscription_status")) if obj.get("subscription_status") is not None else None,
            "credits_used": CreditsUsed1.from_dict(obj.get("credits_used")) if obj.get("credits_used") is not None else None
        })
        return _obj


