# CreateChatPromptResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | [**Name**](Name.md) |  | [optional] 
**chat_id** | **object** |  | 
**metadata** | [**Metadata1**](Metadata1.md) |  | [optional] 
**document_keys** | [**DocumentKeys1**](DocumentKeys1.md) |  | [optional] 
**document_id** | [**DocumentId**](DocumentId.md) |  | [optional] 
**created_at** | **object** |  | 
**custom_agent** | [**CustomAgent**](CustomAgent.md) |  | [optional] 

## Example

```python
from odin_sdk.models.create_chat_prompt_response import CreateChatPromptResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CreateChatPromptResponse from a JSON string
create_chat_prompt_response_instance = CreateChatPromptResponse.from_json(json)
# print the JSON string representation of the object
print CreateChatPromptResponse.to_json()

# convert the object into a dict
create_chat_prompt_response_dict = create_chat_prompt_response_instance.to_dict()
# create an instance of CreateChatPromptResponse from a dict
create_chat_prompt_response_form_dict = create_chat_prompt_response.from_dict(create_chat_prompt_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


