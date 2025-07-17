# CreateChatPromptRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | **object** |  | 
**name** | [**Name**](Name.md) |  | [optional] 
**context** | [**Context**](Context.md) |  | [optional] 
**metadata** | [**Metadata1**](Metadata1.md) |  | [optional] 
**document_keys** | [**DocumentKeys1**](DocumentKeys1.md) |  | [optional] 
**document_id** | [**DocumentId**](DocumentId.md) |  | [optional] 

## Example

```python
from odin_sdk.models.create_chat_prompt_request import CreateChatPromptRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateChatPromptRequest from a JSON string
create_chat_prompt_request_instance = CreateChatPromptRequest.from_json(json)
# print the JSON string representation of the object
print CreateChatPromptRequest.to_json()

# convert the object into a dict
create_chat_prompt_request_dict = create_chat_prompt_request_instance.to_dict()
# create an instance of CreateChatPromptRequest from a dict
create_chat_prompt_request_form_dict = create_chat_prompt_request.from_dict(create_chat_prompt_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


