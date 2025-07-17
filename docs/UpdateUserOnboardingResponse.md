# UpdateUserOnboardingResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **object** |  | 
**message** | **object** |  | 

## Example

```python
from odin_sdk.models.update_user_onboarding_response import UpdateUserOnboardingResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateUserOnboardingResponse from a JSON string
update_user_onboarding_response_instance = UpdateUserOnboardingResponse.from_json(json)
# print the JSON string representation of the object
print UpdateUserOnboardingResponse.to_json()

# convert the object into a dict
update_user_onboarding_response_dict = update_user_onboarding_response_instance.to_dict()
# create an instance of UpdateUserOnboardingResponse from a dict
update_user_onboarding_response_form_dict = update_user_onboarding_response.from_dict(update_user_onboarding_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


