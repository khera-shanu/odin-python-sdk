# DeleteDocumentRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | **object** |  | 
**document_id** | **object** |  | 

## Example

```python
from odin_sdk.models.delete_document_request import DeleteDocumentRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteDocumentRequest from a JSON string
delete_document_request_instance = DeleteDocumentRequest.from_json(json)
# print the JSON string representation of the object
print DeleteDocumentRequest.to_json()

# convert the object into a dict
delete_document_request_dict = delete_document_request_instance.to_dict()
# create an instance of DeleteDocumentRequest from a dict
delete_document_request_form_dict = delete_document_request.from_dict(delete_document_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


