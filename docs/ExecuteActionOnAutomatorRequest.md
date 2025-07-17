# ExecuteActionOnAutomatorRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action_name** | **object** | The name of the action to execute. | 
**flow_id** | **object** | The ID of the action flow. | 
**ui_form** | **object** | The UI form to execute the action with. | [optional] 
**project_id** | **object** | The ID of the project on which to execute the action. | 
**chat_id** | [**ChatId2**](ChatId2.md) |  | [optional] 
**message_id** | [**MessageId2**](MessageId2.md) |  | [optional] 
**return_response** | [**ReturnResponse**](ReturnResponse.md) |  | [optional] 
**type** | [**Type2**](Type2.md) |  | [optional] 
**config** | [**Config3**](Config3.md) |  | [optional] 

## Example

```python
from odin_sdk.models.execute_action_on_automator_request import ExecuteActionOnAutomatorRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ExecuteActionOnAutomatorRequest from a JSON string
execute_action_on_automator_request_instance = ExecuteActionOnAutomatorRequest.from_json(json)
# print the JSON string representation of the object
print ExecuteActionOnAutomatorRequest.to_json()

# convert the object into a dict
execute_action_on_automator_request_dict = execute_action_on_automator_request_instance.to_dict()
# create an instance of ExecuteActionOnAutomatorRequest from a dict
execute_action_on_automator_request_form_dict = execute_action_on_automator_request.from_dict(execute_action_on_automator_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


