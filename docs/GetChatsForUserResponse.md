# GetChatsForUserResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**chats** | [**Chats**](Chats.md) |  | [optional] 
**next_cursor** | [**NextCursor**](NextCursor.md) |  | [optional] 
**has_more** | **object** |  | [optional] 

## Example

```python
from odin_sdk.models.get_chats_for_user_response import GetChatsForUserResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetChatsForUserResponse from a JSON string
get_chats_for_user_response_instance = GetChatsForUserResponse.from_json(json)
# print the JSON string representation of the object
print GetChatsForUserResponse.to_json()

# convert the object into a dict
get_chats_for_user_response_dict = get_chats_for_user_response_instance.to_dict()
# create an instance of GetChatsForUserResponse from a dict
get_chats_for_user_response_form_dict = get_chats_for_user_response.from_dict(get_chats_for_user_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


