# GetChatsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**chats** | [**Chats**](Chats.md) |  | [optional] 
**next_cursor** | [**NextCursor**](NextCursor.md) |  | [optional] 
**has_more** | **object** |  | [optional] 

## Example

```python
from odin_sdk.models.get_chats_response import GetChatsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetChatsResponse from a JSON string
get_chats_response_instance = GetChatsResponse.from_json(json)
# print the JSON string representation of the object
print GetChatsResponse.to_json()

# convert the object into a dict
get_chats_response_dict = get_chats_response_instance.to_dict()
# create an instance of GetChatsResponse from a dict
get_chats_response_form_dict = get_chats_response.from_dict(get_chats_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


