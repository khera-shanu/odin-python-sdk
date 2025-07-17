# RoutesProjectsResponseKBDocument


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **object** | The ID of the document. | 
**content_key** | **object** | The content key of the document - either full URL in case of web links stored in the KB or full filename, e.g. &#39;example.pdf&#39;. | 
**content** | [**Content2**](Content2.md) |  | [optional] 
**metadata** | **object** | The metadata of the document. | 
**doc_type** | **object** | The type of the document. | 
**metadata_extracted** | [**MetadataExtracted**](MetadataExtracted.md) |  | [optional] 
**pii** | [**Pii**](Pii.md) |  | [optional] 
**data_type** | [**DataType1**](DataType1.md) |  | [optional] 
**data_type_id** | [**DataTypeId3**](DataTypeId3.md) |  | [optional] 
**data_type_name** | [**DataTypeName**](DataTypeName.md) |  | [optional] 
**data_type_extracted** | [**DataTypeExtracted**](DataTypeExtracted.md) |  | [optional] 
**document_id** | [**DocumentId2**](DocumentId2.md) |  | [optional] 
**extraction_with_comparison** | [**ExtractionWithComparison1**](ExtractionWithComparison1.md) |  | [optional] 
**extraction_with_confidence_from_llm** | [**ExtractionWithConfidenceFromLlm1**](ExtractionWithConfidenceFromLlm1.md) |  | [optional] 

## Example

```python
from odin_sdk.models.routes_projects_response_kb_document import RoutesProjectsResponseKBDocument

# TODO update the JSON string below
json = "{}"
# create an instance of RoutesProjectsResponseKBDocument from a JSON string
routes_projects_response_kb_document_instance = RoutesProjectsResponseKBDocument.from_json(json)
# print the JSON string representation of the object
print RoutesProjectsResponseKBDocument.to_json()

# convert the object into a dict
routes_projects_response_kb_document_dict = routes_projects_response_kb_document_instance.to_dict()
# create an instance of RoutesProjectsResponseKBDocument from a dict
routes_projects_response_kb_document_form_dict = routes_projects_response_kb_document.from_dict(routes_projects_response_kb_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


