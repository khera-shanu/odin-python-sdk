# TeamInfoDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active** | [**Active1**](Active1.md) |  | [optional] 
**admin** | [**Admin**](Admin.md) |  | [optional] 
**name** | [**Name**](Name.md) |  | [optional] 
**credits** | [**Credits1**](Credits1.md) |  | [optional] 
**used_credits** | [**UsedCredits**](UsedCredits.md) |  | [optional] 
**bonus_credits** | [**BonusCredits**](BonusCredits.md) |  | [optional] 
**allowed_seats** | [**AllowedSeats1**](AllowedSeats1.md) |  | [optional] 
**team_id** | [**TeamId**](TeamId.md) |  | [optional] 
**members** | [**Members3**](Members3.md) |  | [optional] 
**email_domain** | [**EmailDomain**](EmailDomain.md) |  | [optional] 
**owner** | [**Owner**](Owner.md) |  | [optional] 
**plan_type** | [**PlanType1**](PlanType1.md) |  | [optional] 
**api_keys** | [**ApiKeys**](ApiKeys.md) |  | [optional] 
**settings** | [**Settings1**](Settings1.md) |  | [optional] 
**aihub_projects_whitelist** | [**AihubProjectsWhitelist**](AihubProjectsWhitelist.md) |  | [optional] 

## Example

```python
from odin_sdk.models.team_info_details import TeamInfoDetails

# TODO update the JSON string below
json = "{}"
# create an instance of TeamInfoDetails from a JSON string
team_info_details_instance = TeamInfoDetails.from_json(json)
# print the JSON string representation of the object
print TeamInfoDetails.to_json()

# convert the object into a dict
team_info_details_dict = team_info_details_instance.to_dict()
# create an instance of TeamInfoDetails from a dict
team_info_details_form_dict = team_info_details.from_dict(team_info_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


