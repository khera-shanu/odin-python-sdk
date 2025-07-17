# FlowsRules


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**view** | **object** | view permission for flows | [optional] 
**edit** | **object** | edit permission for flows | [optional] 

## Example

```python
from odin_sdk.models.flows_rules import FlowsRules

# TODO update the JSON string below
json = "{}"
# create an instance of FlowsRules from a JSON string
flows_rules_instance = FlowsRules.from_json(json)
# print the JSON string representation of the object
print FlowsRules.to_json()

# convert the object into a dict
flows_rules_dict = flows_rules_instance.to_dict()
# create an instance of FlowsRules from a dict
flows_rules_form_dict = flows_rules.from_dict(flows_rules_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


