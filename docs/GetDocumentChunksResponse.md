# GetDocumentChunksResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**chunks** | **object** | List of content chunks for the document | 
**total_chunks** | **object** | Total number of chunks available | 
**total_pages** | **object** | Total number of pages available | 
**current_page** | **object** | Current page number | 

## Example

```python
from odin_sdk.models.get_document_chunks_response import GetDocumentChunksResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetDocumentChunksResponse from a JSON string
get_document_chunks_response_instance = GetDocumentChunksResponse.from_json(json)
# print the JSON string representation of the object
print GetDocumentChunksResponse.to_json()

# convert the object into a dict
get_document_chunks_response_dict = get_document_chunks_response_instance.to_dict()
# create an instance of GetDocumentChunksResponse from a dict
get_document_chunks_response_form_dict = get_document_chunks_response.from_dict(get_document_chunks_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


