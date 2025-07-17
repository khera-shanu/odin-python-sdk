# UpdateRulesRequestAgents


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**view** | [**View**](View.md) |  | [optional] 
**edit** | [**Edit**](Edit.md) |  | [optional] 

## Example

```python
from odin_sdk.models.update_rules_request_agents import UpdateRulesRequestAgents

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateRulesRequestAgents from a JSON string
update_rules_request_agents_instance = UpdateRulesRequestAgents.from_json(json)
# print the JSON string representation of the object
print UpdateRulesRequestAgents.to_json()

# convert the object into a dict
update_rules_request_agents_dict = update_rules_request_agents_instance.to_dict()
# create an instance of UpdateRulesRequestAgents from a dict
update_rules_request_agents_form_dict = update_rules_request_agents.from_dict(update_rules_request_agents_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


