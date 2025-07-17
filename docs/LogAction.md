# LogAction


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**log_id** | **object** |  | 
**email** | [**Email**](Email.md) |  | [optional] 
**action** | **object** |  | 
**timestamp** | **object** |  | 
**role** | **object** |  | 

## Example

```python
from odin_sdk.models.log_action import LogAction

# TODO update the JSON string below
json = "{}"
# create an instance of LogAction from a JSON string
log_action_instance = LogAction.from_json(json)
# print the JSON string representation of the object
print LogAction.to_json()

# convert the object into a dict
log_action_dict = log_action_instance.to_dict()
# create an instance of LogAction from a dict
log_action_form_dict = log_action.from_dict(log_action_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


