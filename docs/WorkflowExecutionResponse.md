# WorkflowExecutionResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique execution ID | 
**tool_id** | **str** | ID of the tool that was executed (mapped from workflow_id) | 
**project_id** | **str** | Project ID | 
**user_id** | **str** |  | [optional] 
**status** | **str** | Execution status | 
**mode** | [**ExecutionTriggerMode**](ExecutionTriggerMode.md) | Execution mode (manual, scheduled, email, file_upload) | 
**started_at** | **str** | ISO timestamp when execution started | 
**ended_at** | **str** |  | [optional] 
**execution_time_ms** | **int** |  | [optional] 
**tool_config** | **object** |  | [optional] 
**inputs** | **object** | Runtime inputs | [optional] 
**execution_data** | **object** |  | [optional] 
**error_message** | **str** |  | [optional] 
**correlation_id** | **str** |  | [optional] 
**push_ref** | **str** |  | [optional] 
**tool_version** | **str** |  | [optional] 

## Example

```python
from odin_sdk.models.workflow_execution_response import WorkflowExecutionResponse

# TODO update the JSON string below
json = "{}"
# create an instance of WorkflowExecutionResponse from a JSON string
workflow_execution_response_instance = WorkflowExecutionResponse.from_json(json)
# print the JSON string representation of the object
print(WorkflowExecutionResponse.to_json())

# convert the object into a dict
workflow_execution_response_dict = workflow_execution_response_instance.to_dict()
# create an instance of WorkflowExecutionResponse from a dict
workflow_execution_response_from_dict = WorkflowExecutionResponse.from_dict(workflow_execution_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


