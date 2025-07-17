# MessageInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user** | [**User**](User.md) |  | [optional] 
**user_id** | [**UserId1**](UserId1.md) |  | [optional] 
**question** | **object** |  | 
**created_at** | **object** |  | 
**feedback_count** | **object** |  | 
**chat_id** | **object** |  | 
**message_id** | **object** |  | 

## Example

```python
from odin_sdk.models.message_info import MessageInfo

# TODO update the JSON string below
json = "{}"
# create an instance of MessageInfo from a JSON string
message_info_instance = MessageInfo.from_json(json)
# print the JSON string representation of the object
print MessageInfo.to_json()

# convert the object into a dict
message_info_dict = message_info_instance.to_dict()
# create an instance of MessageInfo from a dict
message_info_form_dict = message_info.from_dict(message_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


