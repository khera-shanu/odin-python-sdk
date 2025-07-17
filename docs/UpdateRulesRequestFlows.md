# UpdateRulesRequestFlows


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**view** | [**View**](View.md) |  | [optional] 
**edit** | [**Edit**](Edit.md) |  | [optional] 

## Example

```python
from odin_sdk.models.update_rules_request_flows import UpdateRulesRequestFlows

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateRulesRequestFlows from a JSON string
update_rules_request_flows_instance = UpdateRulesRequestFlows.from_json(json)
# print the JSON string representation of the object
print UpdateRulesRequestFlows.to_json()

# convert the object into a dict
update_rules_request_flows_dict = update_rules_request_flows_instance.to_dict()
# create an instance of UpdateRulesRequestFlows from a dict
update_rules_request_flows_form_dict = update_rules_request_flows.from_dict(update_rules_request_flows_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


