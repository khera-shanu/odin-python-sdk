# SaveVoiceMessageRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | **object** |  | 
**chat_id** | **object** |  | 
**message** | **object** |  | 
**response** | [**Response2**](Response2.md) |  | [optional] 
**user_name** | **object** |  | 
**user_id** | **object** |  | 
**message_type** | **object** |  | 
**agent_id** | [**AgentId**](AgentId.md) |  | [optional] 
**agent_name** | [**AgentName**](AgentName.md) |  | [optional] 
**conversation_id** | [**ConversationId**](ConversationId.md) |  | [optional] 

## Example

```python
from odin_sdk.models.save_voice_message_request import SaveVoiceMessageRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SaveVoiceMessageRequest from a JSON string
save_voice_message_request_instance = SaveVoiceMessageRequest.from_json(json)
# print the JSON string representation of the object
print SaveVoiceMessageRequest.to_json()

# convert the object into a dict
save_voice_message_request_dict = save_voice_message_request_instance.to_dict()
# create an instance of SaveVoiceMessageRequest from a dict
save_voice_message_request_form_dict = save_voice_message_request.from_dict(save_voice_message_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


