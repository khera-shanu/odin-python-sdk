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
from odin_sdk.models.join_at import JoinAt
from odin_sdk.models.media_retention_end import MediaRetentionEnd
from odin_sdk.models.meeting_info import MeetingInfo
from odin_sdk.models.meeting_metadata import MeetingMetadata
from odin_sdk.models.meeting_url import MeetingUrl
from odin_sdk.models.odin_attendees import OdinAttendees
from odin_sdk.models.recording import Recording
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class MeetingData(BaseModel):
    """
    MeetingData
    """ # noqa: E501
    audio_size: Optional[Any]
    credits_used: Optional[Any]
    odin_attendees: Optional[OdinAttendees] = None
    is_calendar_meeting: Optional[Any]
    meeting_url: Optional[MeetingUrl] = None
    media_retention_end: Optional[MediaRetentionEnd] = None
    attendee_emails: Optional[Any]
    status_code: Optional[Any]
    video_url: Optional[Any]
    meeting_info: MeetingInfo
    join_at: Optional[JoinAt] = None
    video_size: Optional[Any]
    calendar_meetings: Optional[Any]
    timestamp: Optional[Any]
    meeting_participants: Optional[Any]
    recording: Optional[Recording] = None
    meeting_duration: Optional[Any]
    meeting_metadata: Optional[MeetingMetadata] = None
    status_changes: Optional[Any]
    id: Optional[Any]
    __properties: ClassVar[List[str]] = ["audio_size", "credits_used", "odin_attendees", "is_calendar_meeting", "meeting_url", "media_retention_end", "attendee_emails", "status_code", "video_url", "meeting_info", "join_at", "video_size", "calendar_meetings", "timestamp", "meeting_participants", "recording", "meeting_duration", "meeting_metadata", "status_changes", "id"]

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
        """Create an instance of MeetingData from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of odin_attendees
        if self.odin_attendees:
            _dict['odin_attendees'] = self.odin_attendees.to_dict()
        # override the default output from pydantic by calling `to_dict()` of meeting_url
        if self.meeting_url:
            _dict['meeting_url'] = self.meeting_url.to_dict()
        # override the default output from pydantic by calling `to_dict()` of media_retention_end
        if self.media_retention_end:
            _dict['media_retention_end'] = self.media_retention_end.to_dict()
        # override the default output from pydantic by calling `to_dict()` of meeting_info
        if self.meeting_info:
            _dict['meeting_info'] = self.meeting_info.to_dict()
        # override the default output from pydantic by calling `to_dict()` of join_at
        if self.join_at:
            _dict['join_at'] = self.join_at.to_dict()
        # override the default output from pydantic by calling `to_dict()` of recording
        if self.recording:
            _dict['recording'] = self.recording.to_dict()
        # override the default output from pydantic by calling `to_dict()` of meeting_metadata
        if self.meeting_metadata:
            _dict['meeting_metadata'] = self.meeting_metadata.to_dict()
        # set to None if audio_size (nullable) is None
        # and model_fields_set contains the field
        if self.audio_size is None and "audio_size" in self.model_fields_set:
            _dict['audio_size'] = None

        # set to None if credits_used (nullable) is None
        # and model_fields_set contains the field
        if self.credits_used is None and "credits_used" in self.model_fields_set:
            _dict['credits_used'] = None

        # set to None if is_calendar_meeting (nullable) is None
        # and model_fields_set contains the field
        if self.is_calendar_meeting is None and "is_calendar_meeting" in self.model_fields_set:
            _dict['is_calendar_meeting'] = None

        # set to None if attendee_emails (nullable) is None
        # and model_fields_set contains the field
        if self.attendee_emails is None and "attendee_emails" in self.model_fields_set:
            _dict['attendee_emails'] = None

        # set to None if status_code (nullable) is None
        # and model_fields_set contains the field
        if self.status_code is None and "status_code" in self.model_fields_set:
            _dict['status_code'] = None

        # set to None if video_url (nullable) is None
        # and model_fields_set contains the field
        if self.video_url is None and "video_url" in self.model_fields_set:
            _dict['video_url'] = None

        # set to None if video_size (nullable) is None
        # and model_fields_set contains the field
        if self.video_size is None and "video_size" in self.model_fields_set:
            _dict['video_size'] = None

        # set to None if calendar_meetings (nullable) is None
        # and model_fields_set contains the field
        if self.calendar_meetings is None and "calendar_meetings" in self.model_fields_set:
            _dict['calendar_meetings'] = None

        # set to None if timestamp (nullable) is None
        # and model_fields_set contains the field
        if self.timestamp is None and "timestamp" in self.model_fields_set:
            _dict['timestamp'] = None

        # set to None if meeting_participants (nullable) is None
        # and model_fields_set contains the field
        if self.meeting_participants is None and "meeting_participants" in self.model_fields_set:
            _dict['meeting_participants'] = None

        # set to None if meeting_duration (nullable) is None
        # and model_fields_set contains the field
        if self.meeting_duration is None and "meeting_duration" in self.model_fields_set:
            _dict['meeting_duration'] = None

        # set to None if status_changes (nullable) is None
        # and model_fields_set contains the field
        if self.status_changes is None and "status_changes" in self.model_fields_set:
            _dict['status_changes'] = None

        # set to None if id (nullable) is None
        # and model_fields_set contains the field
        if self.id is None and "id" in self.model_fields_set:
            _dict['id'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of MeetingData from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "audio_size": obj.get("audio_size"),
            "credits_used": obj.get("credits_used"),
            "odin_attendees": OdinAttendees.from_dict(obj.get("odin_attendees")) if obj.get("odin_attendees") is not None else None,
            "is_calendar_meeting": obj.get("is_calendar_meeting"),
            "meeting_url": MeetingUrl.from_dict(obj.get("meeting_url")) if obj.get("meeting_url") is not None else None,
            "media_retention_end": MediaRetentionEnd.from_dict(obj.get("media_retention_end")) if obj.get("media_retention_end") is not None else None,
            "attendee_emails": obj.get("attendee_emails"),
            "status_code": obj.get("status_code"),
            "video_url": obj.get("video_url"),
            "meeting_info": MeetingInfo.from_dict(obj.get("meeting_info")) if obj.get("meeting_info") is not None else None,
            "join_at": JoinAt.from_dict(obj.get("join_at")) if obj.get("join_at") is not None else None,
            "video_size": obj.get("video_size"),
            "calendar_meetings": obj.get("calendar_meetings"),
            "timestamp": obj.get("timestamp"),
            "meeting_participants": obj.get("meeting_participants"),
            "recording": Recording.from_dict(obj.get("recording")) if obj.get("recording") is not None else None,
            "meeting_duration": obj.get("meeting_duration"),
            "meeting_metadata": MeetingMetadata.from_dict(obj.get("meeting_metadata")) if obj.get("meeting_metadata") is not None else None,
            "status_changes": obj.get("status_changes"),
            "id": obj.get("id")
        })
        return _obj


