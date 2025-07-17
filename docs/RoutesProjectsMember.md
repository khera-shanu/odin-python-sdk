# RoutesProjectsMember


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | [**Id1**](Id1.md) |  | [optional] 
**role** | [**Role1**](Role1.md) |  | [optional] 
**project_id** | [**ProjectId**](ProjectId.md) |  | [optional] 
**user_id** | **object** |  | [optional] 
**name** | [**Name**](Name.md) |  | [optional] 
**email** | [**Email**](Email.md) |  | [optional] 
**is_pending** | [**IsPending1**](IsPending1.md) |  | [optional] 
**invited_by** | [**RoutesProjectsMemberInvitedBy**](RoutesProjectsMemberInvitedBy.md) |  | [optional] 

## Example

```python
from odin_sdk.models.routes_projects_member import RoutesProjectsMember

# TODO update the JSON string below
json = "{}"
# create an instance of RoutesProjectsMember from a JSON string
routes_projects_member_instance = RoutesProjectsMember.from_json(json)
# print the JSON string representation of the object
print RoutesProjectsMember.to_json()

# convert the object into a dict
routes_projects_member_dict = routes_projects_member_instance.to_dict()
# create an instance of RoutesProjectsMember from a dict
routes_projects_member_form_dict = routes_projects_member.from_dict(routes_projects_member_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


