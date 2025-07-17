# CreateChatTestResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**chat_id** | **object** |  | 
**created_at** | **object** |  | 
**name** | **object** |  | 
**expected_answer** | **object** |  | 
**test_group** | [**TestGroup**](TestGroup.md) |  | [optional] 
**messages** | **object** |  | 

## Example

```python
from odin_sdk.models.create_chat_test_response import CreateChatTestResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CreateChatTestResponse from a JSON string
create_chat_test_response_instance = CreateChatTestResponse.from_json(json)
# print the JSON string representation of the object
print CreateChatTestResponse.to_json()

# convert the object into a dict
create_chat_test_response_dict = create_chat_test_response_instance.to_dict()
# create an instance of CreateChatTestResponse from a dict
create_chat_test_response_form_dict = create_chat_test_response.from_dict(create_chat_test_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


