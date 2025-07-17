# ExecuteActionOnFormRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**agent_id** | **object** | The ID of the agent on which to execute the action. | 
**action_name** | **object** | The name of the action to execute. | 
**ui_form** | **object** | The UI form to execute the action with. | [optional] 
**project_id** | **object** | The ID of the project on which to execute the action. | 
**chat_id** | [**ChatId1**](ChatId1.md) |  | [optional] 
**message_id** | [**MessageId1**](MessageId1.md) |  | [optional] 

## Example

```python
from odin_sdk.models.execute_action_on_form_request import ExecuteActionOnFormRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ExecuteActionOnFormRequest from a JSON string
execute_action_on_form_request_instance = ExecuteActionOnFormRequest.from_json(json)
# print the JSON string representation of the object
print ExecuteActionOnFormRequest.to_json()

# convert the object into a dict
execute_action_on_form_request_dict = execute_action_on_form_request_instance.to_dict()
# create an instance of ExecuteActionOnFormRequest from a dict
execute_action_on_form_request_form_dict = execute_action_on_form_request.from_dict(execute_action_on_form_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


