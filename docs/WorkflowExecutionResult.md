# WorkflowExecutionResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** | Whether workflow execution was successful | 
**message** | **str** | Execution result message | 
**node_results** | **object** | Results from each node | [optional] 
**execution_time_ms** | **int** | Total execution time | 
**execution_id** | **str** | Unique execution identifier | 
**error** | **str** |  | [optional] 
**parallel_stats** | **object** | Parallel execution statistics | [optional] 

## Example

```python
from odin_sdk.models.workflow_execution_result import WorkflowExecutionResult

# TODO update the JSON string below
json = "{}"
# create an instance of WorkflowExecutionResult from a JSON string
workflow_execution_result_instance = WorkflowExecutionResult.from_json(json)
# print the JSON string representation of the object
print(WorkflowExecutionResult.to_json())

# convert the object into a dict
workflow_execution_result_dict = workflow_execution_result_instance.to_dict()
# create an instance of WorkflowExecutionResult from a dict
workflow_execution_result_from_dict = WorkflowExecutionResult.from_dict(workflow_execution_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


