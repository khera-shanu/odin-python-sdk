# ProjectMember


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | **object** |  | 
**invited_by** | [**InvitedBy**](InvitedBy.md) |  | 
**is_pending** | [**IsPending1**](IsPending1.md) |  | 
**user_id** | [**UserId1**](UserId1.md) |  | 
**email** | [**Email**](Email.md) |  | 
**role** | [**Role1**](Role1.md) |  | 
**role_id** | [**RoleId1**](RoleId1.md) |  | 
**name** | [**Name**](Name.md) |  | 
**index** | [**Index**](Index.md) |  | 

## Example

```python
from odin_sdk.models.project_member import ProjectMember

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectMember from a JSON string
project_member_instance = ProjectMember.from_json(json)
# print the JSON string representation of the object
print ProjectMember.to_json()

# convert the object into a dict
project_member_dict = project_member_instance.to_dict()
# create an instance of ProjectMember from a dict
project_member_form_dict = project_member.from_dict(project_member_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


