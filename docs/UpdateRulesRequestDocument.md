# UpdateRulesRequestDocument


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**view** | [**View**](View.md) |  | [optional] 
**edit** | [**Edit**](Edit.md) |  | [optional] 

## Example

```python
from odin_sdk.models.update_rules_request_document import UpdateRulesRequestDocument

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateRulesRequestDocument from a JSON string
update_rules_request_document_instance = UpdateRulesRequestDocument.from_json(json)
# print the JSON string representation of the object
print UpdateRulesRequestDocument.to_json()

# convert the object into a dict
update_rules_request_document_dict = update_rules_request_document_instance.to_dict()
# create an instance of UpdateRulesRequestDocument from a dict
update_rules_request_document_form_dict = update_rules_request_document.from_dict(update_rules_request_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


