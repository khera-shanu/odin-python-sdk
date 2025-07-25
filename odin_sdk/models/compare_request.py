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
from odin_sdk.models.credit_usage_limit import CreditUsageLimit
from odin_sdk.models.diff_ai_overide_limit import DiffAiOverideLimit
from odin_sdk.models.doc1_content import Doc1Content
from odin_sdk.models.doc2_content import Doc2Content
from odin_sdk.models.document1 import Document1
from odin_sdk.models.document2 import Document2
from odin_sdk.models.ignore_instructions import IgnoreInstructions
from odin_sdk.models.sent_from_automator1 import SentFromAutomator1
from odin_sdk.models.wait_till_complete import WaitTillComplete
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class CompareRequest(BaseModel):
    """
    CompareRequest
    """ # noqa: E501
    project_id: Optional[Any] = Field(description="The ID of the project on which to execute the action.")
    document_1: Optional[Document1] = None
    document_2: Optional[Document2] = None
    doc_1_content: Optional[Doc1Content] = None
    doc_2_content: Optional[Doc2Content] = None
    ignore_instructions: Optional[IgnoreInstructions] = None
    credit_usage_limit: Optional[CreditUsageLimit] = None
    diff_ai_overide_limit: Optional[DiffAiOverideLimit] = None
    sent_from_automator: Optional[SentFromAutomator1] = None
    wait_till_complete: Optional[WaitTillComplete] = None
    __properties: ClassVar[List[str]] = ["project_id", "document_1", "document_2", "doc_1_content", "doc_2_content", "ignore_instructions", "credit_usage_limit", "diff_ai_overide_limit", "sent_from_automator", "wait_till_complete"]

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
        """Create an instance of CompareRequest from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of document_1
        if self.document_1:
            _dict['document_1'] = self.document_1.to_dict()
        # override the default output from pydantic by calling `to_dict()` of document_2
        if self.document_2:
            _dict['document_2'] = self.document_2.to_dict()
        # override the default output from pydantic by calling `to_dict()` of doc_1_content
        if self.doc_1_content:
            _dict['doc_1_content'] = self.doc_1_content.to_dict()
        # override the default output from pydantic by calling `to_dict()` of doc_2_content
        if self.doc_2_content:
            _dict['doc_2_content'] = self.doc_2_content.to_dict()
        # override the default output from pydantic by calling `to_dict()` of ignore_instructions
        if self.ignore_instructions:
            _dict['ignore_instructions'] = self.ignore_instructions.to_dict()
        # override the default output from pydantic by calling `to_dict()` of credit_usage_limit
        if self.credit_usage_limit:
            _dict['credit_usage_limit'] = self.credit_usage_limit.to_dict()
        # override the default output from pydantic by calling `to_dict()` of diff_ai_overide_limit
        if self.diff_ai_overide_limit:
            _dict['diff_ai_overide_limit'] = self.diff_ai_overide_limit.to_dict()
        # override the default output from pydantic by calling `to_dict()` of sent_from_automator
        if self.sent_from_automator:
            _dict['sent_from_automator'] = self.sent_from_automator.to_dict()
        # override the default output from pydantic by calling `to_dict()` of wait_till_complete
        if self.wait_till_complete:
            _dict['wait_till_complete'] = self.wait_till_complete.to_dict()
        # set to None if project_id (nullable) is None
        # and model_fields_set contains the field
        if self.project_id is None and "project_id" in self.model_fields_set:
            _dict['project_id'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of CompareRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "project_id": obj.get("project_id"),
            "document_1": Document1.from_dict(obj.get("document_1")) if obj.get("document_1") is not None else None,
            "document_2": Document2.from_dict(obj.get("document_2")) if obj.get("document_2") is not None else None,
            "doc_1_content": Doc1Content.from_dict(obj.get("doc_1_content")) if obj.get("doc_1_content") is not None else None,
            "doc_2_content": Doc2Content.from_dict(obj.get("doc_2_content")) if obj.get("doc_2_content") is not None else None,
            "ignore_instructions": IgnoreInstructions.from_dict(obj.get("ignore_instructions")) if obj.get("ignore_instructions") is not None else None,
            "credit_usage_limit": CreditUsageLimit.from_dict(obj.get("credit_usage_limit")) if obj.get("credit_usage_limit") is not None else None,
            "diff_ai_overide_limit": DiffAiOverideLimit.from_dict(obj.get("diff_ai_overide_limit")) if obj.get("diff_ai_overide_limit") is not None else None,
            "sent_from_automator": SentFromAutomator1.from_dict(obj.get("sent_from_automator")) if obj.get("sent_from_automator") is not None else None,
            "wait_till_complete": WaitTillComplete.from_dict(obj.get("wait_till_complete")) if obj.get("wait_till_complete") is not None else None
        })
        return _obj


