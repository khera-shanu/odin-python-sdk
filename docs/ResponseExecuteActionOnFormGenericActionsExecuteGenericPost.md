# ResponseExecuteActionOnFormGenericActionsExecuteGenericPost


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
from odin_sdk.models.response_execute_action_on_form_generic_actions_execute_generic_post import ResponseExecuteActionOnFormGenericActionsExecuteGenericPost

# TODO update the JSON string below
json = "{}"
# create an instance of ResponseExecuteActionOnFormGenericActionsExecuteGenericPost from a JSON string
response_execute_action_on_form_generic_actions_execute_generic_post_instance = ResponseExecuteActionOnFormGenericActionsExecuteGenericPost.from_json(json)
# print the JSON string representation of the object
print ResponseExecuteActionOnFormGenericActionsExecuteGenericPost.to_json()

# convert the object into a dict
response_execute_action_on_form_generic_actions_execute_generic_post_dict = response_execute_action_on_form_generic_actions_execute_generic_post_instance.to_dict()
# create an instance of ResponseExecuteActionOnFormGenericActionsExecuteGenericPost from a dict
response_execute_action_on_form_generic_actions_execute_generic_post_form_dict = response_execute_action_on_form_generic_actions_execute_generic_post.from_dict(response_execute_action_on_form_generic_actions_execute_generic_post_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


