# SubscriptionUpdate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **object** |  | 
**number_of_seats** | **object** |  | 

## Example

```python
from odin_sdk.models.subscription_update import SubscriptionUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of SubscriptionUpdate from a JSON string
subscription_update_instance = SubscriptionUpdate.from_json(json)
# print the JSON string representation of the object
print SubscriptionUpdate.to_json()

# convert the object into a dict
subscription_update_dict = subscription_update_instance.to_dict()
# create an instance of SubscriptionUpdate from a dict
subscription_update_form_dict = subscription_update.from_dict(subscription_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


