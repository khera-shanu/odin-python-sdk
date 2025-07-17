# ResponseAddSharepointFileToKnowledgeBaseProjectKnowledgeAddSharepointPost


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
from odin_sdk.models.response_add_sharepoint_file_to_knowledge_base_project_knowledge_add_sharepoint_post import ResponseAddSharepointFileToKnowledgeBaseProjectKnowledgeAddSharepointPost

# TODO update the JSON string below
json = "{}"
# create an instance of ResponseAddSharepointFileToKnowledgeBaseProjectKnowledgeAddSharepointPost from a JSON string
response_add_sharepoint_file_to_knowledge_base_project_knowledge_add_sharepoint_post_instance = ResponseAddSharepointFileToKnowledgeBaseProjectKnowledgeAddSharepointPost.from_json(json)
# print the JSON string representation of the object
print ResponseAddSharepointFileToKnowledgeBaseProjectKnowledgeAddSharepointPost.to_json()

# convert the object into a dict
response_add_sharepoint_file_to_knowledge_base_project_knowledge_add_sharepoint_post_dict = response_add_sharepoint_file_to_knowledge_base_project_knowledge_add_sharepoint_post_instance.to_dict()
# create an instance of ResponseAddSharepointFileToKnowledgeBaseProjectKnowledgeAddSharepointPost from a dict
response_add_sharepoint_file_to_knowledge_base_project_knowledge_add_sharepoint_post_form_dict = response_add_sharepoint_file_to_knowledge_base_project_knowledge_add_sharepoint_post.from_dict(response_add_sharepoint_file_to_knowledge_base_project_knowledge_add_sharepoint_post_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


