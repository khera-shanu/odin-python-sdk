# Action


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | [**Email**](Email.md) |  | [optional] 
**action** | **object** |  | 
**credits_used** | **object** |  | 
**timestamp** | **object** |  | 
**role** | **object** |  | 

## Example

```python
from odin_sdk.models.action import Action

# TODO update the JSON string below
json = "{}"
# create an instance of Action from a JSON string
action_instance = Action.from_json(json)
# print the JSON string representation of the object
print Action.to_json()

# convert the object into a dict
action_dict = action_instance.to_dict()
# create an instance of Action from a dict
action_form_dict = action.from_dict(action_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


