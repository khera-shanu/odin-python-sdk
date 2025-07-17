# CustomToolListResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tools** | **object** | List of custom tools | 
**total** | **object** | Total number of tools | 

## Example

```python
from odin_sdk.models.custom_tool_list_response import CustomToolListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CustomToolListResponse from a JSON string
custom_tool_list_response_instance = CustomToolListResponse.from_json(json)
# print the JSON string representation of the object
print CustomToolListResponse.to_json()

# convert the object into a dict
custom_tool_list_response_dict = custom_tool_list_response_instance.to_dict()
# create an instance of CustomToolListResponse from a dict
custom_tool_list_response_form_dict = custom_tool_list_response.from_dict(custom_tool_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


