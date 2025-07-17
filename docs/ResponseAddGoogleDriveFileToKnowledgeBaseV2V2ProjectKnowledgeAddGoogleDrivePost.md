# ResponseAddGoogleDriveFileToKnowledgeBaseV2V2ProjectKnowledgeAddGoogleDrivePost


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **object** |  | 
**content** | **object** |  | 
**document_data** | **object** |  | 
**url** | [**Url**](Url.md) |  | [optional] 
**uploaded_by** | [**UploadedBy**](UploadedBy.md) |  | [optional] 
**status** | [**RoutesKnowledgebaseKnowledgeBaseDataResponseStatus**](RoutesKnowledgebaseKnowledgeBaseDataResponseStatus.md) |  | [optional] 
**size** | [**Size**](Size.md) |  | [optional] 
**document_key** | **object** |  | 
**data_type_id** | [**DataTypeId1**](DataTypeId1.md) |  | [optional] 

## Example

```python
from odin_sdk.models.response_add_google_drive_file_to_knowledge_base_v2_v2_project_knowledge_add_google_drive_post import ResponseAddGoogleDriveFileToKnowledgeBaseV2V2ProjectKnowledgeAddGoogleDrivePost

# TODO update the JSON string below
json = "{}"
# create an instance of ResponseAddGoogleDriveFileToKnowledgeBaseV2V2ProjectKnowledgeAddGoogleDrivePost from a JSON string
response_add_google_drive_file_to_knowledge_base_v2_v2_project_knowledge_add_google_drive_post_instance = ResponseAddGoogleDriveFileToKnowledgeBaseV2V2ProjectKnowledgeAddGoogleDrivePost.from_json(json)
# print the JSON string representation of the object
print ResponseAddGoogleDriveFileToKnowledgeBaseV2V2ProjectKnowledgeAddGoogleDrivePost.to_json()

# convert the object into a dict
response_add_google_drive_file_to_knowledge_base_v2_v2_project_knowledge_add_google_drive_post_dict = response_add_google_drive_file_to_knowledge_base_v2_v2_project_knowledge_add_google_drive_post_instance.to_dict()
# create an instance of ResponseAddGoogleDriveFileToKnowledgeBaseV2V2ProjectKnowledgeAddGoogleDrivePost from a dict
response_add_google_drive_file_to_knowledge_base_v2_v2_project_knowledge_add_google_drive_post_form_dict = response_add_google_drive_file_to_knowledge_base_v2_v2_project_knowledge_add_google_drive_post.from_dict(response_add_google_drive_file_to_knowledge_base_v2_v2_project_knowledge_add_google_drive_post_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


