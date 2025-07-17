# MeetingData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**audio_size** | **object** |  | 
**credits_used** | **object** |  | 
**odin_attendees** | [**OdinAttendees**](OdinAttendees.md) |  | [optional] 
**is_calendar_meeting** | **object** |  | 
**meeting_url** | [**MeetingUrl**](MeetingUrl.md) |  | [optional] 
**media_retention_end** | [**MediaRetentionEnd**](MediaRetentionEnd.md) |  | [optional] 
**attendee_emails** | **object** |  | 
**status_code** | **object** |  | 
**video_url** | **object** |  | 
**meeting_info** | [**MeetingInfo**](MeetingInfo.md) |  | 
**join_at** | [**JoinAt**](JoinAt.md) |  | [optional] 
**video_size** | **object** |  | 
**calendar_meetings** | **object** |  | 
**timestamp** | **object** |  | 
**meeting_participants** | **object** |  | 
**recording** | [**Recording**](Recording.md) |  | [optional] 
**meeting_duration** | **object** |  | 
**meeting_metadata** | [**MeetingMetadata**](MeetingMetadata.md) |  | [optional] 
**status_changes** | **object** |  | 
**id** | **object** |  | 

## Example

```python
from odin_sdk.models.meeting_data import MeetingData

# TODO update the JSON string below
json = "{}"
# create an instance of MeetingData from a JSON string
meeting_data_instance = MeetingData.from_json(json)
# print the JSON string representation of the object
print MeetingData.to_json()

# convert the object into a dict
meeting_data_dict = meeting_data_instance.to_dict()
# create an instance of MeetingData from a dict
meeting_data_form_dict = meeting_data.from_dict(meeting_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


