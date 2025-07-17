# UpdateDocumentRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | **object** |  | 
**document_id** | **object** |  | 
**title** | [**Title**](Title.md) |  | [optional] 
**body** | [**Body**](Body.md) |  | [optional] 
**word_count** | [**WordCount**](WordCount.md) |  | [optional] 
**content_key** | [**ContentKey**](ContentKey.md) |  | [optional] 

## Example

```python
from odin_sdk.models.update_document_request import UpdateDocumentRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateDocumentRequest from a JSON string
update_document_request_instance = UpdateDocumentRequest.from_json(json)
# print the JSON string representation of the object
print UpdateDocumentRequest.to_json()

# convert the object into a dict
update_document_request_dict = update_document_request_instance.to_dict()
# create an instance of UpdateDocumentRequest from a dict
update_document_request_form_dict = update_document_request.from_dict(update_document_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


