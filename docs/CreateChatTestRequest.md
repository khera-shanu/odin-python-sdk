# CreateChatTestRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | **object** |  | 
**question** | **object** |  | 
**expected_answer** | [**ExpectedAnswer**](ExpectedAnswer.md) |  | [optional] 
**test_group** | [**TestGroup**](TestGroup.md) |  | [optional] 
**test_group_id** | [**TestGroupId**](TestGroupId.md) |  | [optional] 

## Example

```python
from odin_sdk.models.create_chat_test_request import CreateChatTestRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateChatTestRequest from a JSON string
create_chat_test_request_instance = CreateChatTestRequest.from_json(json)
# print the JSON string representation of the object
print CreateChatTestRequest.to_json()

# convert the object into a dict
create_chat_test_request_dict = create_chat_test_request_instance.to_dict()
# create an instance of CreateChatTestRequest from a dict
create_chat_test_request_form_dict = create_chat_test_request.from_dict(create_chat_test_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


