# UpdateRulesRequestAddMembers


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**view** | [**View**](View.md) |  | [optional] 
**edit** | [**Edit**](Edit.md) |  | [optional] 

## Example

```python
from odin_sdk.models.update_rules_request_add_members import UpdateRulesRequestAddMembers

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateRulesRequestAddMembers from a JSON string
update_rules_request_add_members_instance = UpdateRulesRequestAddMembers.from_json(json)
# print the JSON string representation of the object
print UpdateRulesRequestAddMembers.to_json()

# convert the object into a dict
update_rules_request_add_members_dict = update_rules_request_add_members_instance.to_dict()
# create an instance of UpdateRulesRequestAddMembers from a dict
update_rules_request_add_members_form_dict = update_rules_request_add_members.from_dict(update_rules_request_add_members_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


