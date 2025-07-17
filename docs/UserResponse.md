# UserResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **object** |  | 
**email** | **object** |  | 
**name** | [**Name**](Name.md) |  | 
**is_admin** | **object** |  | [optional] 
**subscription_status** | [**SubscriptionStatus**](SubscriptionStatus.md) |  | [optional] 
**credits_used** | [**CreditsUsed1**](CreditsUsed1.md) |  | [optional] 

## Example

```python
from odin_sdk.models.user_response import UserResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UserResponse from a JSON string
user_response_instance = UserResponse.from_json(json)
# print the JSON string representation of the object
print UserResponse.to_json()

# convert the object into a dict
user_response_dict = user_response_instance.to_dict()
# create an instance of UserResponse from a dict
user_response_form_dict = user_response.from_dict(user_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


