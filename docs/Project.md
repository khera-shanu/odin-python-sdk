# Project


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **object** |  | 
**name** | **object** |  | 
**owner** | [**Owner1**](Owner1.md) |  | [optional] 
**created_at** | [**CreatedAt3**](CreatedAt3.md) |  | [optional] 
**type** | [**Type3**](Type3.md) |  | [optional] 
**model_name** | [**ModelName3**](ModelName3.md) |  | [optional] 
**members** | [**Members**](Members.md) |  | 
**description** | [**Description10**](Description10.md) |  | [optional] 
**is_favorite** | [**IsFavorite**](IsFavorite.md) |  | [optional] 
**kb_info** | [**ProjectKbInfo**](ProjectKbInfo.md) |  | [optional] 
**kb_last_synced** | [**KbLastSynced**](KbLastSynced.md) |  | [optional] 
**kb_status** | [**KbStatus**](KbStatus.md) |  | [optional] 
**kb_sync_schedule** | [**KbSyncSchedule**](KbSyncSchedule.md) |  | [optional] 
**blacklisted_docs** | [**BlacklistedDocs**](BlacklistedDocs.md) |  | [optional] 
**team_id** | [**TeamId**](TeamId.md) |  | [optional] 
**system_prompt** | [**SystemPrompt**](SystemPrompt.md) |  | [optional] 
**custom_agent** | **object** |  | [optional] 
**custom_agent_name** | [**CustomAgentName**](CustomAgentName.md) |  | [optional] 
**updated_at** | [**UpdatedAt**](UpdatedAt.md) |  | [optional] 
**is_public** | [**IsPublic**](IsPublic.md) |  | [optional] 
**use_textract** | [**UseTextract**](UseTextract.md) |  | [optional] 
**mask_pii** | [**MaskPii**](MaskPii.md) |  | [optional] 
**inline_citations** | [**InlineCitations**](InlineCitations.md) |  | [optional] 
**custom_chatbot** | [**ProjectCustomChatbot**](ProjectCustomChatbot.md) |  | [optional] 
**feedback_history** | [**FeedbackHistory**](FeedbackHistory.md) |  | [optional] 
**api_keys** | [**ProjectApiKeys**](ProjectApiKeys.md) |  | [optional] 
**kb_version** | [**KbVersion**](KbVersion.md) |  | [optional] 
**embedding_model** | [**EmbeddingModel**](EmbeddingModel.md) |  | [optional] 
**teamsbot_upload_method** | [**TeamsbotUploadMethod**](TeamsbotUploadMethod.md) |  | [optional] 
**teamsbot_static_message_footer** | [**TeamsbotStaticMessageFooter**](TeamsbotStaticMessageFooter.md) |  | [optional] 
**teamsbot_show_feedback_buttons** | [**TeamsbotShowFeedbackButtons**](TeamsbotShowFeedbackButtons.md) |  | [optional] 
**teamsbot_show_kb_search_message** | [**TeamsbotShowKbSearchMessage**](TeamsbotShowKbSearchMessage.md) |  | [optional] 
**teamsbot_show_message_sources** | [**TeamsbotShowMessageSources**](TeamsbotShowMessageSources.md) |  | [optional] 
**shared_to_team** | [**SharedToTeam**](SharedToTeam.md) |  | [optional] 
**team_default_role** | [**TeamDefaultRole**](TeamDefaultRole.md) |  | [optional] 
**shared** | [**Shared**](Shared.md) |  | [optional] 

## Example

```python
from odin_sdk.models.project import Project

# TODO update the JSON string below
json = "{}"
# create an instance of Project from a JSON string
project_instance = Project.from_json(json)
# print the JSON string representation of the object
print Project.to_json()

# convert the object into a dict
project_dict = project_instance.to_dict()
# create an instance of Project from a dict
project_form_dict = project.from_dict(project_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


