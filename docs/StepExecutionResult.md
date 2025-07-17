# StepExecutionResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **object** | Whether the step execution was successful | 
**message** | **object** | A message describing the result | 
**data** | [**Data**](Data.md) |  | [optional] 
**error** | [**Error2**](Error2.md) |  | [optional] 
**execution_time_ms** | [**ExecutionTimeMs1**](ExecutionTimeMs1.md) |  | [optional] 

## Example

```python
from odin_sdk.models.step_execution_result import StepExecutionResult

# TODO update the JSON string below
json = "{}"
# create an instance of StepExecutionResult from a JSON string
step_execution_result_instance = StepExecutionResult.from_json(json)
# print the JSON string representation of the object
print StepExecutionResult.to_json()

# convert the object into a dict
step_execution_result_dict = step_execution_result_instance.to_dict()
# create an instance of StepExecutionResult from a dict
step_execution_result_form_dict = step_execution_result.from_dict(step_execution_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


