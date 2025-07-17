# UpdateCodeRunnerActionRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | **object** | The project ID | 
**flow_id** | **object** | The flow ID of the action to update | 
**script_name** | **object** | The name of the script | 
**script_description** | [**ScriptDescription**](ScriptDescription.md) |  | [optional] 
**script** | **object** | The script code | 
**runtime** | **object** | Runtime version (e.g., python3.11, nodejs20.x) | 
**entry_point** | **object** | Entry point function name | [optional] 
**kwargs** | **object** | List of keyword argument names (deprecated, use parameters) | [optional] 
**parameters** | [**Parameters**](Parameters.md) |  | [optional] 
**autosend** | [**Autosend1**](Autosend1.md) |  | [optional] 

## Example

```python
from odin_sdk.models.update_code_runner_action_request import UpdateCodeRunnerActionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateCodeRunnerActionRequest from a JSON string
update_code_runner_action_request_instance = UpdateCodeRunnerActionRequest.from_json(json)
# print the JSON string representation of the object
print UpdateCodeRunnerActionRequest.to_json()

# convert the object into a dict
update_code_runner_action_request_dict = update_code_runner_action_request_instance.to_dict()
# create an instance of UpdateCodeRunnerActionRequest from a dict
update_code_runner_action_request_form_dict = update_code_runner_action_request.from_dict(update_code_runner_action_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


