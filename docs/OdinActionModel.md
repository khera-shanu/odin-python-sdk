# OdinActionModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**flow_id** | **object** | The ID of the action flow. | 
**action_name** | **object** | The name of the action. | 
**action_description** | **object** | The description of the action. | 
**required_fields_for_flow** | **object** | The list of fields required for the action flow. | [optional] 
**autosend** | **object** | Whether the action is autosendable or not. | 
**type** | [**Type2**](Type2.md) |  | [optional] 
**config** | [**Config4**](Config4.md) |  | [optional] 

## Example

```python
from odin_sdk.models.odin_action_model import OdinActionModel

# TODO update the JSON string below
json = "{}"
# create an instance of OdinActionModel from a JSON string
odin_action_model_instance = OdinActionModel.from_json(json)
# print the JSON string representation of the object
print OdinActionModel.to_json()

# convert the object into a dict
odin_action_model_dict = odin_action_model_instance.to_dict()
# create an instance of OdinActionModel from a dict
odin_action_model_form_dict = odin_action_model.from_dict(odin_action_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


