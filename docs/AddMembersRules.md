# AddMembersRules


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**view** | **object** | view permission for add_members | [optional] 
**edit** | **object** | edit permission for add_members | [optional] 

## Example

```python
from odin_sdk.models.add_members_rules import AddMembersRules

# TODO update the JSON string below
json = "{}"
# create an instance of AddMembersRules from a JSON string
add_members_rules_instance = AddMembersRules.from_json(json)
# print the JSON string representation of the object
print AddMembersRules.to_json()

# convert the object into a dict
add_members_rules_dict = add_members_rules_instance.to_dict()
# create an instance of AddMembersRules from a dict
add_members_rules_form_dict = add_members_rules.from_dict(add_members_rules_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


