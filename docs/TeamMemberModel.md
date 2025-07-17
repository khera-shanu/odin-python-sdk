# TeamMemberModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**role** | [**Role1**](Role1.md) |  | [optional] 
**uid** | [**Uid**](Uid.md) |  | [optional] 
**is_pending** | [**IsPending**](IsPending.md) |  | [optional] 
**email** | [**Email**](Email.md) |  | [optional] 

## Example

```python
from odin_sdk.models.team_member_model import TeamMemberModel

# TODO update the JSON string below
json = "{}"
# create an instance of TeamMemberModel from a JSON string
team_member_model_instance = TeamMemberModel.from_json(json)
# print the JSON string representation of the object
print TeamMemberModel.to_json()

# convert the object into a dict
team_member_model_dict = team_member_model_instance.to_dict()
# create an instance of TeamMemberModel from a dict
team_member_model_form_dict = team_member_model.from_dict(team_member_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


