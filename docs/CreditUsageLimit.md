# CreditUsageLimit

The maximum number of credits to use.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from odin_sdk.models.credit_usage_limit import CreditUsageLimit

# TODO update the JSON string below
json = "{}"
# create an instance of CreditUsageLimit from a JSON string
credit_usage_limit_instance = CreditUsageLimit.from_json(json)
# print the JSON string representation of the object
print CreditUsageLimit.to_json()

# convert the object into a dict
credit_usage_limit_dict = credit_usage_limit_instance.to_dict()
# create an instance of CreditUsageLimit from a dict
credit_usage_limit_form_dict = credit_usage_limit.from_dict(credit_usage_limit_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


