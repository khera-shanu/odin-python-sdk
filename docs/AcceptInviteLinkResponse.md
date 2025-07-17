# AcceptInviteLinkResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **object** |  | 
**project_id** | [**ProjectId**](ProjectId.md) |  | [optional] 

## Example

```python
from odin_sdk.models.accept_invite_link_response import AcceptInviteLinkResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AcceptInviteLinkResponse from a JSON string
accept_invite_link_response_instance = AcceptInviteLinkResponse.from_json(json)
# print the JSON string representation of the object
print AcceptInviteLinkResponse.to_json()

# convert the object into a dict
accept_invite_link_response_dict = accept_invite_link_response_instance.to_dict()
# create an instance of AcceptInviteLinkResponse from a dict
accept_invite_link_response_form_dict = accept_invite_link_response.from_dict(accept_invite_link_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


