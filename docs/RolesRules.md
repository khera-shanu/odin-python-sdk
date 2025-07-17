# RolesRules


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**view** | **object** | view permission for roles | [optional] 
**edit** | **object** | edit permission for roles | [optional] 

## Example

```python
from odin_sdk.models.roles_rules import RolesRules

# TODO update the JSON string below
json = "{}"
# create an instance of RolesRules from a JSON string
roles_rules_instance = RolesRules.from_json(json)
# print the JSON string representation of the object
print RolesRules.to_json()

# convert the object into a dict
roles_rules_dict = roles_rules_instance.to_dict()
# create an instance of RolesRules from a dict
roles_rules_form_dict = roles_rules.from_dict(roles_rules_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


