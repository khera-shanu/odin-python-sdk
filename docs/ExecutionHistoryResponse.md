# ExecutionHistoryResponse

Response model for execution history

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**executions** | **object** |  | 
**total** | **object** |  | 
**page** | **object** |  | 
**page_size** | **object** |  | 

## Example

```python
from odin_sdk.models.execution_history_response import ExecutionHistoryResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ExecutionHistoryResponse from a JSON string
execution_history_response_instance = ExecutionHistoryResponse.from_json(json)
# print the JSON string representation of the object
print ExecutionHistoryResponse.to_json()

# convert the object into a dict
execution_history_response_dict = execution_history_response_instance.to_dict()
# create an instance of ExecutionHistoryResponse from a dict
execution_history_response_form_dict = execution_history_response.from_dict(execution_history_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


