# TestExecuteResponse

Response model for test execution

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **object** |  | 
**result** | [**Result**](Result.md) |  | [optional] 
**error** | [**Error**](Error.md) |  | [optional] 
**error_type** | [**ErrorType**](ErrorType.md) |  | [optional] 
**error_traceback** | [**ErrorTraceback**](ErrorTraceback.md) |  | [optional] 
**execution_time_ms** | [**ExecutionTimeMs**](ExecutionTimeMs.md) |  | [optional] 
**memory_used_mb** | [**MemoryUsedMb**](MemoryUsedMb.md) |  | [optional] 
**logs** | [**Logs**](Logs.md) |  | [optional] 
**function_name** | **object** |  | 
**stdout** | [**Stdout**](Stdout.md) |  | [optional] 
**stderr** | [**Stderr**](Stderr.md) |  | [optional] 

## Example

```python
from odin_sdk.models.test_execute_response import TestExecuteResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TestExecuteResponse from a JSON string
test_execute_response_instance = TestExecuteResponse.from_json(json)
# print the JSON string representation of the object
print TestExecuteResponse.to_json()

# convert the object into a dict
test_execute_response_dict = test_execute_response_instance.to_dict()
# create an instance of TestExecuteResponse from a dict
test_execute_response_form_dict = test_execute_response.from_dict(test_execute_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


