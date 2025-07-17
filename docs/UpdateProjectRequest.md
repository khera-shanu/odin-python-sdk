# UpdateProjectRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | **object** |  | 
**name** | [**Name**](Name.md) |  | [optional] 
**type** | [**Type5**](Type5.md) |  | [optional] 
**model_name** | [**ModelName4**](ModelName4.md) |  | [optional] 
**enrich_question** | [**EnrichQuestion**](EnrichQuestion.md) |  | [optional] 
**enrich_sources** | [**EnrichSources**](EnrichSources.md) |  | [optional] 
**description** | [**Description1**](Description1.md) |  | [optional] 
**test_info** | [**TestInfo**](TestInfo.md) |  | [optional] 
**is_public** | [**IsPublic2**](IsPublic2.md) |  | [optional] 
**no_context_answer** | [**NoContextAnswer**](NoContextAnswer.md) |  | [optional] 
**only_answer_with_context** | [**OnlyAnswerWithContext**](OnlyAnswerWithContext.md) |  | [optional] 
**custom_chatbot** | [**CustomChatbot**](CustomChatbot.md) |  | [optional] 
**use_textract** | [**UseTextract1**](UseTextract1.md) |  | [optional] 
**mask_pii** | [**MaskPii1**](MaskPii1.md) |  | [optional] 
**inline_citations** | [**InlineCitations1**](InlineCitations1.md) |  | [optional] 
**data_extraction_method** | [**DataExtractionMethod**](DataExtractionMethod.md) |  | [optional] 
**teamsbot_upload_method** | [**TeamsbotUploadMethod**](TeamsbotUploadMethod.md) |  | [optional] 
**teamsbot_static_message_footer** | [**TeamsbotStaticMessageFooter**](TeamsbotStaticMessageFooter.md) |  | [optional] 
**teamsbot_show_feedback_buttons** | [**TeamsbotShowFeedbackButtons**](TeamsbotShowFeedbackButtons.md) |  | [optional] 
**teamsbot_show_kb_search_message** | [**TeamsbotShowKbSearchMessage**](TeamsbotShowKbSearchMessage.md) |  | [optional] 
**teamsbot_show_message_sources** | [**TeamsbotShowMessageSources**](TeamsbotShowMessageSources.md) |  | [optional] 
**enable_temporary_message_retention** | [**EnableTemporaryMessageRetention**](EnableTemporaryMessageRetention.md) |  | [optional] 
**temporary_message_retention_duration** | [**TemporaryMessageRetentionDuration**](TemporaryMessageRetentionDuration.md) |  | [optional] 
**docx_extraction_method** | [**DocxExtractionMethod**](DocxExtractionMethod.md) |  | [optional] 
**shared_to_team** | [**SharedToTeam**](SharedToTeam.md) |  | [optional] 
**team_default_role** | [**TeamDefaultRole**](TeamDefaultRole.md) |  | [optional] 
**team_id** | [**TeamId**](TeamId.md) |  | [optional] 

## Example

```python
from odin_sdk.models.update_project_request import UpdateProjectRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateProjectRequest from a JSON string
update_project_request_instance = UpdateProjectRequest.from_json(json)
# print the JSON string representation of the object
print UpdateProjectRequest.to_json()

# convert the object into a dict
update_project_request_dict = update_project_request_instance.to_dict()
# create an instance of UpdateProjectRequest from a dict
update_project_request_form_dict = update_project_request.from_dict(update_project_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


