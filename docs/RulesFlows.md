# RulesFlows


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**view** | **object** | view permission for flows | [optional] 
**edit** | **object** | edit permission for flows | [optional] 

## Example

```python
from odin_sdk.models.rules_flows import RulesFlows

# TODO update the JSON string below
json = "{}"
# create an instance of RulesFlows from a JSON string
rules_flows_instance = RulesFlows.from_json(json)
# print the JSON string representation of the object
print RulesFlows.to_json()

# convert the object into a dict
rules_flows_dict = rules_flows_instance.to_dict()
# create an instance of RulesFlows from a dict
rules_flows_form_dict = rules_flows.from_dict(rules_flows_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


