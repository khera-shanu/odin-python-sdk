# ExecuteScriptResponse

Response model for script execution

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **object** |  | 
**result** | [**Result**](Result.md) |  | [optional] 
**error** | [**Error**](Error.md) |  | [optional] 
**execution_time_ms** | [**ExecutionTimeMs**](ExecutionTimeMs.md) |  | [optional] 
**version** | **object** |  | 
**lambda_function_name** | **object** |  | 
**execution_id** | [**ExecutionId**](ExecutionId.md) |  | [optional] 
**stdout** | [**Stdout**](Stdout.md) |  | [optional] 
**stderr** | [**Stderr**](Stderr.md) |  | [optional] 

## Example

```python
from odin_sdk.models.execute_script_response import ExecuteScriptResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ExecuteScriptResponse from a JSON string
execute_script_response_instance = ExecuteScriptResponse.from_json(json)
# print the JSON string representation of the object
print ExecuteScriptResponse.to_json()

# convert the object into a dict
execute_script_response_dict = execute_script_response_instance.to_dict()
# create an instance of ExecuteScriptResponse from a dict
execute_script_response_form_dict = execute_script_response.from_dict(execute_script_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


