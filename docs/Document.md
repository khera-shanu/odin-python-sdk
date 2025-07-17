# Document


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | [**Id1**](Id1.md) |  | [optional] 
**title** | [**Title**](Title.md) |  | [optional] 
**body** | [**Body**](Body.md) |  | [optional] 
**word_count** | [**WordCount**](WordCount.md) |  | [optional] 
**content_key** | [**ContentKey**](ContentKey.md) |  | [optional] 
**created_at** | [**CreatedAt**](CreatedAt.md) |  | [optional] 
**updated_at** | [**UpdatedAt**](UpdatedAt.md) |  | [optional] 

## Example

```python
from odin_sdk.models.document import Document

# TODO update the JSON string below
json = "{}"
# create an instance of Document from a JSON string
document_instance = Document.from_json(json)
# print the JSON string representation of the object
print Document.to_json()

# convert the object into a dict
document_dict = document_instance.to_dict()
# create an instance of Document from a dict
document_form_dict = document.from_dict(document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


