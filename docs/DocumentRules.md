# DocumentRules


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**edit** | **object** | create permission for document | [optional] 
**view** | **object** | view permission for documents | [optional] 

## Example

```python
from odin_sdk.models.document_rules import DocumentRules

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentRules from a JSON string
document_rules_instance = DocumentRules.from_json(json)
# print the JSON string representation of the object
print DocumentRules.to_json()

# convert the object into a dict
document_rules_dict = document_rules_instance.to_dict()
# create an instance of DocumentRules from a dict
document_rules_form_dict = document_rules.from_dict(document_rules_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


