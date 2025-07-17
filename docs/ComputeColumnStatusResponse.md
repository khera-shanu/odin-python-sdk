# ComputeColumnStatusResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **object** |  | 
**execution_id** | **object** |  | 
**status** | **object** |  | 
**progress_percentage** | **object** |  | 
**processed_rows** | **object** |  | 
**total_rows** | [**TotalRows**](TotalRows.md) |  | 
**updated_rows** | **object** |  | 
**failed_rows** | **object** |  | 
**started_at** | [**StartedAt**](StartedAt.md) |  | 
**completed_at** | [**CompletedAt**](CompletedAt.md) |  | 
**error_message** | [**ErrorMessage**](ErrorMessage.md) |  | 
**metadata** | **object** |  | 

## Example

```python
from odin_sdk.models.compute_column_status_response import ComputeColumnStatusResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ComputeColumnStatusResponse from a JSON string
compute_column_status_response_instance = ComputeColumnStatusResponse.from_json(json)
# print the JSON string representation of the object
print ComputeColumnStatusResponse.to_json()

# convert the object into a dict
compute_column_status_response_dict = compute_column_status_response_instance.to_dict()
# create an instance of ComputeColumnStatusResponse from a dict
compute_column_status_response_form_dict = compute_column_status_response.from_dict(compute_column_status_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


