# ValidateInviteLinkResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_valid** | **object** |  | 
**project_id** | [**ProjectId**](ProjectId.md) |  | [optional] 
**project_name** | [**ProjectName**](ProjectName.md) |  | [optional] 
**project_description** | [**ProjectDescription**](ProjectDescription.md) |  | [optional] 
**role_id** | [**RoleId1**](RoleId1.md) |  | [optional] 
**message** | **object** |  | 

## Example

```python
from odin_sdk.models.validate_invite_link_response import ValidateInviteLinkResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ValidateInviteLinkResponse from a JSON string
validate_invite_link_response_instance = ValidateInviteLinkResponse.from_json(json)
# print the JSON string representation of the object
print ValidateInviteLinkResponse.to_json()

# convert the object into a dict
validate_invite_link_response_dict = validate_invite_link_response_instance.to_dict()
# create an instance of ValidateInviteLinkResponse from a dict
validate_invite_link_response_form_dict = validate_invite_link_response.from_dict(validate_invite_link_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


