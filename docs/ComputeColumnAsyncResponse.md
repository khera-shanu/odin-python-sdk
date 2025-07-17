# ComputeColumnAsyncResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **object** |  | 
**execution_id** | **object** |  | 
**status** | **object** |  | [optional] 
**estimated_duration** | [**EstimatedDuration**](EstimatedDuration.md) |  | [optional] 

## Example

```python
from odin_sdk.models.compute_column_async_response import ComputeColumnAsyncResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ComputeColumnAsyncResponse from a JSON string
compute_column_async_response_instance = ComputeColumnAsyncResponse.from_json(json)
# print the JSON string representation of the object
print ComputeColumnAsyncResponse.to_json()

# convert the object into a dict
compute_column_async_response_dict = compute_column_async_response_instance.to_dict()
# create an instance of ComputeColumnAsyncResponse from a dict
compute_column_async_response_form_dict = compute_column_async_response.from_dict(compute_column_async_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


