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
from odin_sdk.models.update_rules_request_actions import UpdateRulesRequestActions
from odin_sdk.models.update_rules_request_add_members import UpdateRulesRequestAddMembers
from odin_sdk.models.update_rules_request_agents import UpdateRulesRequestAgents
from odin_sdk.models.update_rules_request_analytics import UpdateRulesRequestAnalytics
from odin_sdk.models.update_rules_request_assistant import UpdateRulesRequestAssistant
from odin_sdk.models.update_rules_request_chat import UpdateRulesRequestChat
from odin_sdk.models.update_rules_request_document import UpdateRulesRequestDocument
from odin_sdk.models.update_rules_request_flows import UpdateRulesRequestFlows
from odin_sdk.models.update_rules_request_kb import UpdateRulesRequestKb
from odin_sdk.models.update_rules_request_roles import UpdateRulesRequestRoles
from odin_sdk.models.update_rules_request_settings import UpdateRulesRequestSettings
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class UpdateRulesRequest(BaseModel):
    """
    UpdateRulesRequest
    """ # noqa: E501
    chat: Optional[UpdateRulesRequestChat] = None
    assistant: Optional[UpdateRulesRequestAssistant] = None
    document: Optional[UpdateRulesRequestDocument] = None
    agents: Optional[UpdateRulesRequestAgents] = None
    settings: Optional[UpdateRulesRequestSettings] = None
    add_members: Optional[UpdateRulesRequestAddMembers] = None
    kb: Optional[UpdateRulesRequestKb] = None
    flows: Optional[UpdateRulesRequestFlows] = None
    analytics: Optional[UpdateRulesRequestAnalytics] = None
    actions: Optional[UpdateRulesRequestActions] = None
    roles: Optional[UpdateRulesRequestRoles] = None
    __properties: ClassVar[List[str]] = ["chat", "assistant", "document", "agents", "settings", "add_members", "kb", "flows", "analytics", "actions", "roles"]

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
        """Create an instance of UpdateRulesRequest from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of chat
        if self.chat:
            _dict['chat'] = self.chat.to_dict()
        # override the default output from pydantic by calling `to_dict()` of assistant
        if self.assistant:
            _dict['assistant'] = self.assistant.to_dict()
        # override the default output from pydantic by calling `to_dict()` of document
        if self.document:
            _dict['document'] = self.document.to_dict()
        # override the default output from pydantic by calling `to_dict()` of agents
        if self.agents:
            _dict['agents'] = self.agents.to_dict()
        # override the default output from pydantic by calling `to_dict()` of settings
        if self.settings:
            _dict['settings'] = self.settings.to_dict()
        # override the default output from pydantic by calling `to_dict()` of add_members
        if self.add_members:
            _dict['add_members'] = self.add_members.to_dict()
        # override the default output from pydantic by calling `to_dict()` of kb
        if self.kb:
            _dict['kb'] = self.kb.to_dict()
        # override the default output from pydantic by calling `to_dict()` of flows
        if self.flows:
            _dict['flows'] = self.flows.to_dict()
        # override the default output from pydantic by calling `to_dict()` of analytics
        if self.analytics:
            _dict['analytics'] = self.analytics.to_dict()
        # override the default output from pydantic by calling `to_dict()` of actions
        if self.actions:
            _dict['actions'] = self.actions.to_dict()
        # override the default output from pydantic by calling `to_dict()` of roles
        if self.roles:
            _dict['roles'] = self.roles.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of UpdateRulesRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "chat": UpdateRulesRequestChat.from_dict(obj.get("chat")) if obj.get("chat") is not None else None,
            "assistant": UpdateRulesRequestAssistant.from_dict(obj.get("assistant")) if obj.get("assistant") is not None else None,
            "document": UpdateRulesRequestDocument.from_dict(obj.get("document")) if obj.get("document") is not None else None,
            "agents": UpdateRulesRequestAgents.from_dict(obj.get("agents")) if obj.get("agents") is not None else None,
            "settings": UpdateRulesRequestSettings.from_dict(obj.get("settings")) if obj.get("settings") is not None else None,
            "add_members": UpdateRulesRequestAddMembers.from_dict(obj.get("add_members")) if obj.get("add_members") is not None else None,
            "kb": UpdateRulesRequestKb.from_dict(obj.get("kb")) if obj.get("kb") is not None else None,
            "flows": UpdateRulesRequestFlows.from_dict(obj.get("flows")) if obj.get("flows") is not None else None,
            "analytics": UpdateRulesRequestAnalytics.from_dict(obj.get("analytics")) if obj.get("analytics") is not None else None,
            "actions": UpdateRulesRequestActions.from_dict(obj.get("actions")) if obj.get("actions") is not None else None,
            "roles": UpdateRulesRequestRoles.from_dict(obj.get("roles")) if obj.get("roles") is not None else None
        })
        return _obj


