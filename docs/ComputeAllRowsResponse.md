# ComputeAllRowsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **object** |  | 
**total_rows_processed** | **object** |  | 
**total_columns_updated** | **object** |  | 
**updated_columns** | **object** |  | 
**failed_rows** | **object** |  | 
**stopped_due_to_failures** | **object** |  | 
**retry_attempts** | **Dict[str, object]** |  | 
**computation_id** | [**ComputationId**](ComputationId.md) |  | [optional] 
**history_table** | [**HistoryTable**](HistoryTable.md) |  | [optional] 
**task_id** | [**TaskId**](TaskId.md) |  | [optional] 

## Example

```python
from odin_sdk.models.compute_all_rows_response import ComputeAllRowsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ComputeAllRowsResponse from a JSON string
compute_all_rows_response_instance = ComputeAllRowsResponse.from_json(json)
# print the JSON string representation of the object
print ComputeAllRowsResponse.to_json()

# convert the object into a dict
compute_all_rows_response_dict = compute_all_rows_response_instance.to_dict()
# create an instance of ComputeAllRowsResponse from a dict
compute_all_rows_response_form_dict = compute_all_rows_response.from_dict(compute_all_rows_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


