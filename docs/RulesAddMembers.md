# RulesAddMembers


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**view** | **object** | view permission for add_members | [optional] 
**edit** | **object** | edit permission for add_members | [optional] 

## Example

```python
from odin_sdk.models.rules_add_members import RulesAddMembers

# TODO update the JSON string below
json = "{}"
# create an instance of RulesAddMembers from a JSON string
rules_add_members_instance = RulesAddMembers.from_json(json)
# print the JSON string representation of the object
print RulesAddMembers.to_json()

# convert the object into a dict
rules_add_members_dict = rules_add_members_instance.to_dict()
# create an instance of RulesAddMembers from a dict
rules_add_members_form_dict = rules_add_members.from_dict(rules_add_members_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


