# UpdateSettingsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**local_signups** | [**LocalSignups**](LocalSignups.md) |  | [optional] 
**team_name** | [**TeamName**](TeamName.md) |  | [optional] 
**disable_meetings** | [**DisableMeetings**](DisableMeetings.md) |  | [optional] 
**default_project_id** | [**DefaultProjectId**](DefaultProjectId.md) |  | [optional] 
**aihub_projects_whitelist** | [**AihubProjectsWhitelist**](AihubProjectsWhitelist.md) |  | [optional] 
**auto_add_users_by_domain** | [**AutoAddUsersByDomain1**](AutoAddUsersByDomain1.md) |  | [optional] 
**team_email_domain** | [**TeamEmailDomain**](TeamEmailDomain.md) |  | [optional] 
**chat_mode_appearance** | [**ChatModeAppearance**](ChatModeAppearance.md) |  | [optional] 
**chat_mode_for_members** | [**ChatModeForMembers**](ChatModeForMembers.md) |  | [optional] 
**enable_user_credit_limits** | [**EnableUserCreditLimits**](EnableUserCreditLimits.md) |  | [optional] 
**default_user_credit_limit** | [**DefaultUserCreditLimit**](DefaultUserCreditLimit.md) |  | [optional] 
**tags** | [**Tags**](Tags.md) |  | [optional] 

## Example

```python
from odin_sdk.models.update_settings_request import UpdateSettingsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateSettingsRequest from a JSON string
update_settings_request_instance = UpdateSettingsRequest.from_json(json)
# print the JSON string representation of the object
print UpdateSettingsRequest.to_json()

# convert the object into a dict
update_settings_request_dict = update_settings_request_instance.to_dict()
# create an instance of UpdateSettingsRequest from a dict
update_settings_request_form_dict = update_settings_request.from_dict(update_settings_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


