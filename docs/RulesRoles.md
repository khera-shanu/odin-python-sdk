# RulesRoles


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**view** | **object** | view permission for roles | [optional] 
**edit** | **object** | edit permission for roles | [optional] 

## Example

```python
from odin_sdk.models.rules_roles import RulesRoles

# TODO update the JSON string below
json = "{}"
# create an instance of RulesRoles from a JSON string
rules_roles_instance = RulesRoles.from_json(json)
# print the JSON string representation of the object
print RulesRoles.to_json()

# convert the object into a dict
rules_roles_dict = rules_roles_instance.to_dict()
# create an instance of RulesRoles from a dict
rules_roles_form_dict = rules_roles.from_dict(rules_roles_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


