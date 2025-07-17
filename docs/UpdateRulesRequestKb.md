# UpdateRulesRequestKb


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**view** | [**View**](View.md) |  | [optional] 
**edit** | [**Edit**](Edit.md) |  | [optional] 

## Example

```python
from odin_sdk.models.update_rules_request_kb import UpdateRulesRequestKb

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateRulesRequestKb from a JSON string
update_rules_request_kb_instance = UpdateRulesRequestKb.from_json(json)
# print the JSON string representation of the object
print UpdateRulesRequestKb.to_json()

# convert the object into a dict
update_rules_request_kb_dict = update_rules_request_kb_instance.to_dict()
# create an instance of UpdateRulesRequestKb from a dict
update_rules_request_kb_form_dict = update_rules_request_kb.from_dict(update_rules_request_kb_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


