# KnowledgeBaseSettingsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | **object** |  | 
**google_search** | **object** |  | [optional] 
**project_documents** | **object** |  | [optional] 

## Example

```python
from odin_sdk.models.knowledge_base_settings_request import KnowledgeBaseSettingsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of KnowledgeBaseSettingsRequest from a JSON string
knowledge_base_settings_request_instance = KnowledgeBaseSettingsRequest.from_json(json)
# print the JSON string representation of the object
print KnowledgeBaseSettingsRequest.to_json()

# convert the object into a dict
knowledge_base_settings_request_dict = knowledge_base_settings_request_instance.to_dict()
# create an instance of KnowledgeBaseSettingsRequest from a dict
knowledge_base_settings_request_form_dict = knowledge_base_settings_request.from_dict(knowledge_base_settings_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


