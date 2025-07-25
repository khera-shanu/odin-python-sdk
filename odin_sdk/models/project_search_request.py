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
from odin_sdk.models.add_bonus_from_full_content import AddBonusFromFullContent
from odin_sdk.models.bonus_from_full_content_size import BonusFromFullContentSize
from odin_sdk.models.bonus_from_full_content_threshold import BonusFromFullContentThreshold
from odin_sdk.models.debug import Debug
from odin_sdk.models.document_keys2 import DocumentKeys2
from odin_sdk.models.full_content_words_limit import FullContentWordsLimit
from odin_sdk.models.generate_ai_summary import GenerateAiSummary
from odin_sdk.models.group_on_backend import GroupOnBackend
from odin_sdk.models.kw_curve_multihit import KwCurveMultihit
from odin_sdk.models.max_results import MaxResults
from odin_sdk.models.metadata_weighting import MetadataWeighting
from odin_sdk.models.multihit_weighting import MultihitWeighting
from odin_sdk.models.page import Page
from odin_sdk.models.project_search_request_metadata_filters import ProjectSearchRequestMetadataFilters
from odin_sdk.models.remove_duplicates import RemoveDuplicates
from odin_sdk.models.search_by_titles import SearchByTitles
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class ProjectSearchRequest(BaseModel):
    """
    ProjectSearchRequest
    """ # noqa: E501
    project_id: Optional[Any]
    query: Optional[Any]
    document_keys: Optional[DocumentKeys2] = None
    hybrid_search_lambda: Optional[Any] = None
    score_threshold: Optional[Any] = None
    kw_fuzzy_threshold: Optional[Any] = None
    kw_curve_multihit: Optional[KwCurveMultihit] = None
    metadata_filters: Optional[ProjectSearchRequestMetadataFilters] = None
    max_results: Optional[MaxResults] = None
    full_content_words_limit: Optional[FullContentWordsLimit] = None
    metadata_weighting: Optional[MetadataWeighting] = None
    remove_duplicates: Optional[RemoveDuplicates] = None
    page: Optional[Page] = None
    debug: Optional[Debug] = None
    generate_ai_summary: Optional[GenerateAiSummary] = None
    search_by_titles: Optional[SearchByTitles] = None
    group_on_backend: Optional[GroupOnBackend] = None
    multihit_weighting: Optional[MultihitWeighting] = None
    add_bonus_from_full_content: Optional[AddBonusFromFullContent] = None
    bonus_from_full_content_threshold: Optional[BonusFromFullContentThreshold] = None
    bonus_from_full_content_size: Optional[BonusFromFullContentSize] = None
    __properties: ClassVar[List[str]] = ["project_id", "query", "document_keys", "hybrid_search_lambda", "score_threshold", "kw_fuzzy_threshold", "kw_curve_multihit", "metadata_filters", "max_results", "full_content_words_limit", "metadata_weighting", "remove_duplicates", "page", "debug", "generate_ai_summary", "search_by_titles", "group_on_backend", "multihit_weighting", "add_bonus_from_full_content", "bonus_from_full_content_threshold", "bonus_from_full_content_size"]

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
        """Create an instance of ProjectSearchRequest from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of document_keys
        if self.document_keys:
            _dict['document_keys'] = self.document_keys.to_dict()
        # override the default output from pydantic by calling `to_dict()` of kw_curve_multihit
        if self.kw_curve_multihit:
            _dict['kw_curve_multihit'] = self.kw_curve_multihit.to_dict()
        # override the default output from pydantic by calling `to_dict()` of metadata_filters
        if self.metadata_filters:
            _dict['metadata_filters'] = self.metadata_filters.to_dict()
        # override the default output from pydantic by calling `to_dict()` of max_results
        if self.max_results:
            _dict['max_results'] = self.max_results.to_dict()
        # override the default output from pydantic by calling `to_dict()` of full_content_words_limit
        if self.full_content_words_limit:
            _dict['full_content_words_limit'] = self.full_content_words_limit.to_dict()
        # override the default output from pydantic by calling `to_dict()` of metadata_weighting
        if self.metadata_weighting:
            _dict['metadata_weighting'] = self.metadata_weighting.to_dict()
        # override the default output from pydantic by calling `to_dict()` of remove_duplicates
        if self.remove_duplicates:
            _dict['remove_duplicates'] = self.remove_duplicates.to_dict()
        # override the default output from pydantic by calling `to_dict()` of page
        if self.page:
            _dict['page'] = self.page.to_dict()
        # override the default output from pydantic by calling `to_dict()` of debug
        if self.debug:
            _dict['debug'] = self.debug.to_dict()
        # override the default output from pydantic by calling `to_dict()` of generate_ai_summary
        if self.generate_ai_summary:
            _dict['generate_ai_summary'] = self.generate_ai_summary.to_dict()
        # override the default output from pydantic by calling `to_dict()` of search_by_titles
        if self.search_by_titles:
            _dict['search_by_titles'] = self.search_by_titles.to_dict()
        # override the default output from pydantic by calling `to_dict()` of group_on_backend
        if self.group_on_backend:
            _dict['group_on_backend'] = self.group_on_backend.to_dict()
        # override the default output from pydantic by calling `to_dict()` of multihit_weighting
        if self.multihit_weighting:
            _dict['multihit_weighting'] = self.multihit_weighting.to_dict()
        # override the default output from pydantic by calling `to_dict()` of add_bonus_from_full_content
        if self.add_bonus_from_full_content:
            _dict['add_bonus_from_full_content'] = self.add_bonus_from_full_content.to_dict()
        # override the default output from pydantic by calling `to_dict()` of bonus_from_full_content_threshold
        if self.bonus_from_full_content_threshold:
            _dict['bonus_from_full_content_threshold'] = self.bonus_from_full_content_threshold.to_dict()
        # override the default output from pydantic by calling `to_dict()` of bonus_from_full_content_size
        if self.bonus_from_full_content_size:
            _dict['bonus_from_full_content_size'] = self.bonus_from_full_content_size.to_dict()
        # set to None if project_id (nullable) is None
        # and model_fields_set contains the field
        if self.project_id is None and "project_id" in self.model_fields_set:
            _dict['project_id'] = None

        # set to None if query (nullable) is None
        # and model_fields_set contains the field
        if self.query is None and "query" in self.model_fields_set:
            _dict['query'] = None

        # set to None if hybrid_search_lambda (nullable) is None
        # and model_fields_set contains the field
        if self.hybrid_search_lambda is None and "hybrid_search_lambda" in self.model_fields_set:
            _dict['hybrid_search_lambda'] = None

        # set to None if score_threshold (nullable) is None
        # and model_fields_set contains the field
        if self.score_threshold is None and "score_threshold" in self.model_fields_set:
            _dict['score_threshold'] = None

        # set to None if kw_fuzzy_threshold (nullable) is None
        # and model_fields_set contains the field
        if self.kw_fuzzy_threshold is None and "kw_fuzzy_threshold" in self.model_fields_set:
            _dict['kw_fuzzy_threshold'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of ProjectSearchRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "project_id": obj.get("project_id"),
            "query": obj.get("query"),
            "document_keys": DocumentKeys2.from_dict(obj.get("document_keys")) if obj.get("document_keys") is not None else None,
            "hybrid_search_lambda": obj.get("hybrid_search_lambda"),
            "score_threshold": obj.get("score_threshold"),
            "kw_fuzzy_threshold": obj.get("kw_fuzzy_threshold"),
            "kw_curve_multihit": KwCurveMultihit.from_dict(obj.get("kw_curve_multihit")) if obj.get("kw_curve_multihit") is not None else None,
            "metadata_filters": ProjectSearchRequestMetadataFilters.from_dict(obj.get("metadata_filters")) if obj.get("metadata_filters") is not None else None,
            "max_results": MaxResults.from_dict(obj.get("max_results")) if obj.get("max_results") is not None else None,
            "full_content_words_limit": FullContentWordsLimit.from_dict(obj.get("full_content_words_limit")) if obj.get("full_content_words_limit") is not None else None,
            "metadata_weighting": MetadataWeighting.from_dict(obj.get("metadata_weighting")) if obj.get("metadata_weighting") is not None else None,
            "remove_duplicates": RemoveDuplicates.from_dict(obj.get("remove_duplicates")) if obj.get("remove_duplicates") is not None else None,
            "page": Page.from_dict(obj.get("page")) if obj.get("page") is not None else None,
            "debug": Debug.from_dict(obj.get("debug")) if obj.get("debug") is not None else None,
            "generate_ai_summary": GenerateAiSummary.from_dict(obj.get("generate_ai_summary")) if obj.get("generate_ai_summary") is not None else None,
            "search_by_titles": SearchByTitles.from_dict(obj.get("search_by_titles")) if obj.get("search_by_titles") is not None else None,
            "group_on_backend": GroupOnBackend.from_dict(obj.get("group_on_backend")) if obj.get("group_on_backend") is not None else None,
            "multihit_weighting": MultihitWeighting.from_dict(obj.get("multihit_weighting")) if obj.get("multihit_weighting") is not None else None,
            "add_bonus_from_full_content": AddBonusFromFullContent.from_dict(obj.get("add_bonus_from_full_content")) if obj.get("add_bonus_from_full_content") is not None else None,
            "bonus_from_full_content_threshold": BonusFromFullContentThreshold.from_dict(obj.get("bonus_from_full_content_threshold")) if obj.get("bonus_from_full_content_threshold") is not None else None,
            "bonus_from_full_content_size": BonusFromFullContentSize.from_dict(obj.get("bonus_from_full_content_size")) if obj.get("bonus_from_full_content_size") is not None else None
        })
        return _obj


