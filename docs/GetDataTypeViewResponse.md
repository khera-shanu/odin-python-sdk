# GetDataTypeViewResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **object** |  | 
**data_view** | **object** |  | 
**data_schema** | **object** |  | 
**views** | **object** |  | 
**pagination** | [**Pagination**](Pagination.md) |  | [optional] 
**total_count** | [**TotalCount**](TotalCount.md) |  | [optional] 

## Example

```python
from odin_sdk.models.get_data_type_view_response import GetDataTypeViewResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetDataTypeViewResponse from a JSON string
get_data_type_view_response_instance = GetDataTypeViewResponse.from_json(json)
# print the JSON string representation of the object
print GetDataTypeViewResponse.to_json()

# convert the object into a dict
get_data_type_view_response_dict = get_data_type_view_response_instance.to_dict()
# create an instance of GetDataTypeViewResponse from a dict
get_data_type_view_response_form_dict = get_data_type_view_response.from_dict(get_data_type_view_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


