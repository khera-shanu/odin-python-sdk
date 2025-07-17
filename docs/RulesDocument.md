# RulesDocument


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**edit** | **object** | create permission for document | [optional] 
**view** | **object** | view permission for documents | [optional] 

## Example

```python
from odin_sdk.models.rules_document import RulesDocument

# TODO update the JSON string below
json = "{}"
# create an instance of RulesDocument from a JSON string
rules_document_instance = RulesDocument.from_json(json)
# print the JSON string representation of the object
print RulesDocument.to_json()

# convert the object into a dict
rules_document_dict = rules_document_instance.to_dict()
# create an instance of RulesDocument from a dict
rules_document_form_dict = rules_document.from_dict(rules_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


