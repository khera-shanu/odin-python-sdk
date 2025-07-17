# UpdateUserOnboardingRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**first_name** | [**Firstname**](Firstname.md) |  | [optional] 
**last_name** | [**Lastname**](Lastname.md) |  | [optional] 
**company_name** | [**Companyname**](Companyname.md) |  | [optional] 
**company_size** | [**Companysize**](Companysize.md) |  | [optional] 
**department** | [**Department**](Department.md) |  | [optional] 
**goal** | [**Goal**](Goal.md) |  | [optional] 
**work_apps** | [**Workapps**](Workapps.md) |  | [optional] 
**onboarding_completed** | [**Onboardingcompleted**](Onboardingcompleted.md) |  | [optional] 

## Example

```python
from odin_sdk.models.update_user_onboarding_request import UpdateUserOnboardingRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateUserOnboardingRequest from a JSON string
update_user_onboarding_request_instance = UpdateUserOnboardingRequest.from_json(json)
# print the JSON string representation of the object
print UpdateUserOnboardingRequest.to_json()

# convert the object into a dict
update_user_onboarding_request_dict = update_user_onboarding_request_instance.to_dict()
# create an instance of UpdateUserOnboardingRequest from a dict
update_user_onboarding_request_form_dict = update_user_onboarding_request.from_dict(update_user_onboarding_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


