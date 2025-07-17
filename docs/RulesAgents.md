# RulesAgents


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**view** | **object** | view permission for agents | [optional] 
**edit** | **object** | edit permission for agents | [optional] 

## Example

```python
from odin_sdk.models.rules_agents import RulesAgents

# TODO update the JSON string below
json = "{}"
# create an instance of RulesAgents from a JSON string
rules_agents_instance = RulesAgents.from_json(json)
# print the JSON string representation of the object
print RulesAgents.to_json()

# convert the object into a dict
rules_agents_dict = rules_agents_instance.to_dict()
# create an instance of RulesAgents from a dict
rules_agents_form_dict = rules_agents.from_dict(rules_agents_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


