# GetDocumentsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **object** |  | 
**documents** | **object** |  | 

## Example

```python
from odin_sdk.models.get_documents_response import GetDocumentsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetDocumentsResponse from a JSON string
get_documents_response_instance = GetDocumentsResponse.from_json(json)
# print the JSON string representation of the object
print GetDocumentsResponse.to_json()

# convert the object into a dict
get_documents_response_dict = get_documents_response_instance.to_dict()
# create an instance of GetDocumentsResponse from a dict
get_documents_response_form_dict = get_documents_response.from_dict(get_documents_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


