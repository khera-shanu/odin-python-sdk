# UpdateTeamMemberRoleRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **object** |  | 
**role** | **object** |  | 

## Example

```python
from odin_sdk.models.update_team_member_role_request import UpdateTeamMemberRoleRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateTeamMemberRoleRequest from a JSON string
update_team_member_role_request_instance = UpdateTeamMemberRoleRequest.from_json(json)
# print the JSON string representation of the object
print UpdateTeamMemberRoleRequest.to_json()

# convert the object into a dict
update_team_member_role_request_dict = update_team_member_role_request_instance.to_dict()
# create an instance of UpdateTeamMemberRoleRequest from a dict
update_team_member_role_request_form_dict = update_team_member_role_request.from_dict(update_team_member_role_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


