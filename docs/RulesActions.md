# RulesActions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**view** | **object** | view permission for actions | [optional] 
**edit** | **object** | edit permission for actions | [optional] 

## Example

```python
from odin_sdk.models.rules_actions import RulesActions

# TODO update the JSON string below
json = "{}"
# create an instance of RulesActions from a JSON string
rules_actions_instance = RulesActions.from_json(json)
# print the JSON string representation of the object
print RulesActions.to_json()

# convert the object into a dict
rules_actions_dict = rules_actions_instance.to_dict()
# create an instance of RulesActions from a dict
rules_actions_form_dict = rules_actions.from_dict(rules_actions_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


