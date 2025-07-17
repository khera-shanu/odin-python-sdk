# ExecuteActionOnFormResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **object** | The message of the response. | 
**success** | **object** | Whether the action was executed successfully or not. | 
**chat_id** | [**ChatId3**](ChatId3.md) |  | [optional] 
**message_id** | [**MessageId3**](MessageId3.md) |  | [optional] 
**flow_run_id** | [**FlowRunId**](FlowRunId.md) |  | [optional] 
**action_response** | [**ActionResponse**](ActionResponse.md) |  | [optional] 

## Example

```python
from odin_sdk.models.execute_action_on_form_response import ExecuteActionOnFormResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ExecuteActionOnFormResponse from a JSON string
execute_action_on_form_response_instance = ExecuteActionOnFormResponse.from_json(json)
# print the JSON string representation of the object
print ExecuteActionOnFormResponse.to_json()

# convert the object into a dict
execute_action_on_form_response_dict = execute_action_on_form_response_instance.to_dict()
# create an instance of ExecuteActionOnFormResponse from a dict
execute_action_on_form_response_form_dict = execute_action_on_form_response.from_dict(execute_action_on_form_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


