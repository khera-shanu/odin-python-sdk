# UserEventResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **object** |  | 
**events** | **object** |  | 
**has_more** | **object** |  | [optional] 
**next_timestamp** | [**NextTimestamp**](NextTimestamp.md) |  | [optional] 

## Example

```python
from odin_sdk.models.user_event_response import UserEventResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UserEventResponse from a JSON string
user_event_response_instance = UserEventResponse.from_json(json)
# print the JSON string representation of the object
print UserEventResponse.to_json()

# convert the object into a dict
user_event_response_dict = user_event_response_instance.to_dict()
# create an instance of UserEventResponse from a dict
user_event_response_form_dict = user_event_response.from_dict(user_event_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


