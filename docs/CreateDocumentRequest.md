# CreateDocumentRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | **object** |  | 
**title** | [**Title**](Title.md) |  | [optional] 
**body** | [**Body**](Body.md) |  | [optional] 
**format** | [**Format**](Format.md) |  | [optional] 
**word_count** | [**WordCount**](WordCount.md) |  | [optional] 
**content_key** | [**ContentKey**](ContentKey.md) |  | [optional] 

## Example

```python
from odin_sdk.models.create_document_request import CreateDocumentRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateDocumentRequest from a JSON string
create_document_request_instance = CreateDocumentRequest.from_json(json)
# print the JSON string representation of the object
print CreateDocumentRequest.to_json()

# convert the object into a dict
create_document_request_dict = create_document_request_instance.to_dict()
# create an instance of CreateDocumentRequest from a dict
create_document_request_form_dict = create_document_request.from_dict(create_document_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


