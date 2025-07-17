# MeetingStorageResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_storage_size** | **object** |  | 

## Example

```python
from odin_sdk.models.meeting_storage_response import MeetingStorageResponse

# TODO update the JSON string below
json = "{}"
# create an instance of MeetingStorageResponse from a JSON string
meeting_storage_response_instance = MeetingStorageResponse.from_json(json)
# print the JSON string representation of the object
print MeetingStorageResponse.to_json()

# convert the object into a dict
meeting_storage_response_dict = meeting_storage_response_instance.to_dict()
# create an instance of MeetingStorageResponse from a dict
meeting_storage_response_form_dict = meeting_storage_response.from_dict(meeting_storage_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


