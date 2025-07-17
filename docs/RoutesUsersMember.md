# RoutesUsersMember


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | [**Email**](Email.md) |  | [optional] 
**uid** | **object** |  | 
**name** | [**Name**](Name.md) |  | [optional] 
**role** | [**Role1**](Role1.md) |  | [optional] 
**is_pending** | [**IsPending1**](IsPending1.md) |  | [optional] 
**credit_limit** | [**CreditLimit**](CreditLimit.md) |  | [optional] 
**credit_limit_override** | [**CreditLimitOverride**](CreditLimitOverride.md) |  | [optional] 
**credits_used** | [**CreditsUsed2**](CreditsUsed2.md) |  | [optional] 

## Example

```python
from odin_sdk.models.routes_users_member import RoutesUsersMember

# TODO update the JSON string below
json = "{}"
# create an instance of RoutesUsersMember from a JSON string
routes_users_member_instance = RoutesUsersMember.from_json(json)
# print the JSON string representation of the object
print RoutesUsersMember.to_json()

# convert the object into a dict
routes_users_member_dict = routes_users_member_instance.to_dict()
# create an instance of RoutesUsersMember from a dict
routes_users_member_form_dict = routes_users_member.from_dict(routes_users_member_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


