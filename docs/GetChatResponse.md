# GetChatResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **object** |  | 
**metadata** | [**Metadata1**](Metadata1.md) |  | [optional] 
**created_at** | [**CreatedAt**](CreatedAt.md) |  | [optional] 
**messages** | [**Messages**](Messages.md) |  | [optional] 
**name** | [**Name**](Name.md) |  | [optional] 
**document_id** | [**DocumentId**](DocumentId.md) |  | [optional] 
**document_keys** | [**DocumentKeys1**](DocumentKeys1.md) |  | [optional] 
**custom_agent** | [**CustomAgent**](CustomAgent.md) |  | [optional] 
**chat_files_metadata** | [**ChatFilesMetadata**](ChatFilesMetadata.md) |  | [optional] 
**debug_prompt_info** | [**DebugPromptInfo**](DebugPromptInfo.md) |  | [optional] 

## Example

```python
from odin_sdk.models.get_chat_response import GetChatResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetChatResponse from a JSON string
get_chat_response_instance = GetChatResponse.from_json(json)
# print the JSON string representation of the object
print GetChatResponse.to_json()

# convert the object into a dict
get_chat_response_dict = get_chat_response_instance.to_dict()
# create an instance of GetChatResponse from a dict
get_chat_response_form_dict = get_chat_response.from_dict(get_chat_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


