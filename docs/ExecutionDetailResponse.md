# ExecutionDetailResponse

Response model for detailed execution information

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **object** |  | 
**code_script_id** | **object** |  | 
**version** | **object** |  | 
**execution_status** | **object** |  | 
**execution_time_ms** | [**ExecutionTimeMs**](ExecutionTimeMs.md) |  | 
**memory_used_mb** | [**MemoryUsedMb**](MemoryUsedMb.md) |  | 
**started_at** | **object** |  | 
**completed_at** | [**CompletedAt1**](CompletedAt1.md) |  | 
**error_message** | [**ErrorMessage**](ErrorMessage.md) |  | 
**error_type** | [**ErrorType**](ErrorType.md) |  | 
**error_traceback** | [**ErrorTraceback**](ErrorTraceback.md) |  | 
**args** | [**Args**](Args.md) |  | 
**kwargs** | [**Kwargs**](Kwargs.md) |  | 
**result** | [**Result**](Result.md) |  | 
**stdout** | [**Stdout**](Stdout.md) |  | 
**stderr** | [**Stderr**](Stderr.md) |  | 

## Example

```python
from odin_sdk.models.execution_detail_response import ExecutionDetailResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ExecutionDetailResponse from a JSON string
execution_detail_response_instance = ExecutionDetailResponse.from_json(json)
# print the JSON string representation of the object
print ExecutionDetailResponse.to_json()

# convert the object into a dict
execution_detail_response_dict = execution_detail_response_instance.to_dict()
# create an instance of ExecutionDetailResponse from a dict
execution_detail_response_form_dict = execution_detail_response.from_dict(execution_detail_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


