# RoutesProjectsKnowledgeBaseDataResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **object** |  | 
**content** | **object** |  | 
**document_data** | **object** |  | 
**url** | [**Url**](Url.md) |  | [optional] 
**uploaded_by** | [**UploadedBy**](UploadedBy.md) |  | [optional] 
**status** | [**Status**](Status.md) |  | [optional] 
**size** | [**Size**](Size.md) |  | [optional] 
**document_key** | **object** |  | 
**data_type_id** | [**DataTypeId1**](DataTypeId1.md) |  | [optional] 

## Example

```python
from odin_sdk.models.routes_projects_knowledge_base_data_response import RoutesProjectsKnowledgeBaseDataResponse

# TODO update the JSON string below
json = "{}"
# create an instance of RoutesProjectsKnowledgeBaseDataResponse from a JSON string
routes_projects_knowledge_base_data_response_instance = RoutesProjectsKnowledgeBaseDataResponse.from_json(json)
# print the JSON string representation of the object
print RoutesProjectsKnowledgeBaseDataResponse.to_json()

# convert the object into a dict
routes_projects_knowledge_base_data_response_dict = routes_projects_knowledge_base_data_response_instance.to_dict()
# create an instance of RoutesProjectsKnowledgeBaseDataResponse from a dict
routes_projects_knowledge_base_data_response_form_dict = routes_projects_knowledge_base_data_response.from_dict(routes_projects_knowledge_base_data_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


