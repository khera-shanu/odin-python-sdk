# MeetingInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **object** |  | 
**ical_uid** | **object** |  | 
**is_recurring** | **object** |  | 
**visibility** | [**Visibility**](Visibility.md) |  | [optional] 
**webex_invite** | [**WebexInvite**](WebexInvite.md) |  | [optional] 
**override_should_record** | [**OverrideShouldRecord**](OverrideShouldRecord.md) |  | [optional] 
**end_time** | **object** |  | 
**id** | **object** |  | 
**meeting_platform** | **object** |  | 
**calendar_platform** | **object** |  | 
**is_hosted_by_me** | **object** |  | 
**attendees_emails** | [**AttendeesEmails**](AttendeesEmails.md) |  | [optional] 
**attendees** | [**Attendees**](Attendees.md) |  | [optional] 
**organizer_email** | **object** |  | 
**teams_invite** | [**TeamsInvite**](TeamsInvite.md) |  | [optional] 
**bot_id** | **object** |  | 
**platform** | **object** |  | 
**meet_invite** | **object** |  | 
**is_external** | **object** |  | 
**zoom_invite** | [**ZoomInvite**](ZoomInvite.md) |  | [optional] 
**will_record_reason** | **object** |  | 
**will_record** | **object** |  | 
**start_time** | **object** |  | 

## Example

```python
from odin_sdk.models.meeting_info import MeetingInfo

# TODO update the JSON string below
json = "{}"
# create an instance of MeetingInfo from a JSON string
meeting_info_instance = MeetingInfo.from_json(json)
# print the JSON string representation of the object
print MeetingInfo.to_json()

# convert the object into a dict
meeting_info_dict = meeting_info_instance.to_dict()
# create an instance of MeetingInfo from a dict
meeting_info_form_dict = meeting_info.from_dict(meeting_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


