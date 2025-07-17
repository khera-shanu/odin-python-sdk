# OnboardingTeamInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**has_team** | **object** |  | 
**team_name** | [**Teamname**](Teamname.md) |  | [optional] 
**company_name** | [**Companyname**](Companyname.md) |  | [optional] 
**company_size** | [**Companysize**](Companysize.md) |  | [optional] 
**department** | [**Department**](Department.md) |  | [optional] 
**member_count** | [**Membercount**](Membercount.md) |  | [optional] 

## Example

```python
from odin_sdk.models.onboarding_team_info import OnboardingTeamInfo

# TODO update the JSON string below
json = "{}"
# create an instance of OnboardingTeamInfo from a JSON string
onboarding_team_info_instance = OnboardingTeamInfo.from_json(json)
# print the JSON string representation of the object
print OnboardingTeamInfo.to_json()

# convert the object into a dict
onboarding_team_info_dict = onboarding_team_info_instance.to_dict()
# create an instance of OnboardingTeamInfo from a dict
onboarding_team_info_form_dict = onboarding_team_info.from_dict(onboarding_team_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


