# CustomToolVersionResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **object** | Version history record ID | 
**tool_id** | **object** | ID of the tool this version belongs to | 
**version** | **object** | Version number | 
**name** | **object** | Tool name at time of publication | 
**description** | [**Description7**](Description7.md) |  | [optional] 
**inputs** | **object** | Tool inputs at time of publication | 
**steps** | **object** | Tool steps at time of publication | 
**published_by** | **object** | User who published this version | 
**published_at** | **object** | Publication timestamp | 
**change_log** | [**ChangeLog**](ChangeLog.md) |  | [optional] 

## Example

```python
from odin_sdk.models.custom_tool_version_response import CustomToolVersionResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CustomToolVersionResponse from a JSON string
custom_tool_version_response_instance = CustomToolVersionResponse.from_json(json)
# print the JSON string representation of the object
print CustomToolVersionResponse.to_json()

# convert the object into a dict
custom_tool_version_response_dict = custom_tool_version_response_instance.to_dict()
# create an instance of CustomToolVersionResponse from a dict
custom_tool_version_response_form_dict = custom_tool_version_response.from_dict(custom_tool_version_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


