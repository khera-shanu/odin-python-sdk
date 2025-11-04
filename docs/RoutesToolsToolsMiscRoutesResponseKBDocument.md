# RoutesToolsToolsMiscRoutesResponseKBDocument


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**content_key** | **str** | The content key of the document - either full URL in case of web links stored in the KB or full filename, e.g. &#39;example.pdf&#39;. | 
**content** | **str** | The content of the document. | 
**metadata** | **object** | The metadata of the document. | 
**doc_type** | **str** | The type of the document. | 

## Example

```python
from odin_sdk.models.routes_tools_tools_misc_routes_response_kb_document import RoutesToolsToolsMiscRoutesResponseKBDocument

# TODO update the JSON string below
json = "{}"
# create an instance of RoutesToolsToolsMiscRoutesResponseKBDocument from a JSON string
routes_tools_tools_misc_routes_response_kb_document_instance = RoutesToolsToolsMiscRoutesResponseKBDocument.from_json(json)
# print the JSON string representation of the object
print(RoutesToolsToolsMiscRoutesResponseKBDocument.to_json())

# convert the object into a dict
routes_tools_tools_misc_routes_response_kb_document_dict = routes_tools_tools_misc_routes_response_kb_document_instance.to_dict()
# create an instance of RoutesToolsToolsMiscRoutesResponseKBDocument from a dict
routes_tools_tools_misc_routes_response_kb_document_from_dict = RoutesToolsToolsMiscRoutesResponseKBDocument.from_dict(routes_tools_tools_misc_routes_response_kb_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


