# SendMessageRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **object** |  | 
**project_id** | **object** |  | 
**chat_id** | [**ChatId**](ChatId.md) |  | [optional] 
**document_keys** | [**DocumentKeys1**](DocumentKeys1.md) |  | [optional] 
**google_search** | [**GoogleSearch**](GoogleSearch.md) |  | [optional] 
**is_test** | [**IsTest**](IsTest.md) |  | [optional] 
**personality_name** | [**PersonalityName**](PersonalityName.md) |  | [optional] 
**return_message** | [**ReturnMessage**](ReturnMessage.md) |  | [optional] 
**ai_response** | [**AiResponse**](AiResponse.md) |  | [optional] 
**model_name** | [**ModelName**](ModelName.md) |  | [optional] 
**agent_type** | [**AgentType**](AgentType.md) |  | [optional] 
**chat_name** | [**ChatName1**](ChatName1.md) |  | [optional] 
**agent_id** | [**AgentId**](AgentId.md) |  | [optional] 
**personality_id** | [**PersonalityId**](PersonalityId.md) |  | [optional] 
**use_knowledgebase** | [**UseKnowledgebase**](UseKnowledgebase.md) |  | [optional] 
**is_regenerating** | [**IsRegenerating**](IsRegenerating.md) |  | [optional] 
**message_id** | [**MessageId**](MessageId.md) |  | [optional] 
**ui_form** | [**UiForm**](UiForm.md) |  | [optional] 
**images** | [**Images1**](Images1.md) |  | [optional] 
**format_instructions** | [**FormatInstructions**](FormatInstructions.md) |  | [optional] 
**ignore_chat_history** | [**IgnoreChatHistory**](IgnoreChatHistory.md) |  | [optional] 
**example_json** | [**ExampleJson**](ExampleJson.md) |  | [optional] 
**is_teams_bot** | [**IsTeamsBot**](IsTeamsBot.md) |  | [optional] 
**sent_from_automator** | [**SentFromAutomator**](SentFromAutomator.md) |  | [optional] 
**skip_stream** | [**SkipStream**](SkipStream.md) |  | [optional] 
**request_metadata** | [**RequestMetadata**](RequestMetadata.md) |  | [optional] 
**artifact** | [**SendMessageRequestArtifact**](SendMessageRequestArtifact.md) |  | [optional] 

## Example

```python
from odin_sdk.models.send_message_request import SendMessageRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SendMessageRequest from a JSON string
send_message_request_instance = SendMessageRequest.from_json(json)
# print the JSON string representation of the object
print SendMessageRequest.to_json()

# convert the object into a dict
send_message_request_dict = send_message_request_instance.to_dict()
# create an instance of SendMessageRequest from a dict
send_message_request_form_dict = send_message_request.from_dict(send_message_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


