# ExecutionHistoryItem

Model for execution history item

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

## Example

```python
from odin_sdk.models.execution_history_item import ExecutionHistoryItem

# TODO update the JSON string below
json = "{}"
# create an instance of ExecutionHistoryItem from a JSON string
execution_history_item_instance = ExecutionHistoryItem.from_json(json)
# print the JSON string representation of the object
print ExecutionHistoryItem.to_json()

# convert the object into a dict
execution_history_item_dict = execution_history_item_instance.to_dict()
# create an instance of ExecutionHistoryItem from a dict
execution_history_item_form_dict = execution_history_item.from_dict(execution_history_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


