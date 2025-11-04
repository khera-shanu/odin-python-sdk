# WorkflowExecutionRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | **str** | The project ID | 
**tool_id** | **str** | The tool ID | 
**tool_config** | **object** |  | [optional] 
**inputs** | **object** | Runtime inputs | [optional] 
**execution_mode** | [**ExecutionMode**](ExecutionMode.md) | execution mode: &#39;workflow&#39; or &#39;debug&#39; | [optional] 
**mode** | [**ExecutionTriggerMode**](ExecutionTriggerMode.md) | Execution trigger mode: &#39;manual&#39;, &#39;scheduled&#39;, &#39;email&#39;, or &#39;file_upload&#39; | [optional] 
**push_ref** | **str** |  | [optional] 
**chat_id** | **str** |  | [optional] 
**message_id** | **str** |  | [optional] 

## Example

```python
from odin_sdk.models.workflow_execution_request import WorkflowExecutionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of WorkflowExecutionRequest from a JSON string
workflow_execution_request_instance = WorkflowExecutionRequest.from_json(json)
# print the JSON string representation of the object
print(WorkflowExecutionRequest.to_json())

# convert the object into a dict
workflow_execution_request_dict = workflow_execution_request_instance.to_dict()
# create an instance of WorkflowExecutionRequest from a dict
workflow_execution_request_from_dict = WorkflowExecutionRequest.from_dict(workflow_execution_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


