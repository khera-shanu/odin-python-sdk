# SaveActionRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | **object** | The ID of the project on which to save the action. | 
**flow_id** | **object** | The unique ID of the action flow. | 
**action_name** | **object** | The name of the action. | 
**action_description** | **object** | The description of the action. | 
**required_fields_for_flow** | **object** | The list of fields required for the action flow. | [optional] 
**is_test** | **object** | Whether the endpoint is being hit in test mode or not. | [optional] 
**confirm_button_label** | [**ConfirmButtonLabel**](ConfirmButtonLabel.md) |  | [optional] 
**cancel_button_label** | [**CancelButtonLabel**](CancelButtonLabel.md) |  | [optional] 
**autosend** | [**Autosend**](Autosend.md) |  | [optional] 
**type** | [**Type2**](Type2.md) |  | [optional] 
**config** | [**Config3**](Config3.md) |  | [optional] 

## Example

```python
from odin_sdk.models.save_action_request import SaveActionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SaveActionRequest from a JSON string
save_action_request_instance = SaveActionRequest.from_json(json)
# print the JSON string representation of the object
print SaveActionRequest.to_json()

# convert the object into a dict
save_action_request_dict = save_action_request_instance.to_dict()
# create an instance of SaveActionRequest from a dict
save_action_request_form_dict = save_action_request.from_dict(save_action_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


