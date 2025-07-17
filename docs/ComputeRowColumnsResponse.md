# ComputeRowColumnsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **object** |  | 
**updated_columns** | **object** |  | 

## Example

```python
from odin_sdk.models.compute_row_columns_response import ComputeRowColumnsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ComputeRowColumnsResponse from a JSON string
compute_row_columns_response_instance = ComputeRowColumnsResponse.from_json(json)
# print the JSON string representation of the object
print ComputeRowColumnsResponse.to_json()

# convert the object into a dict
compute_row_columns_response_dict = compute_row_columns_response_instance.to_dict()
# create an instance of ComputeRowColumnsResponse from a dict
compute_row_columns_response_form_dict = compute_row_columns_response.from_dict(compute_row_columns_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


