# ApiToolRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | **object** | The ID of the project | 
**config** | [**Config**](Config.md) |  | [optional] 

## Example

```python
from odin_sdk.models.api_tool_request import ApiToolRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiToolRequest from a JSON string
api_tool_request_instance = ApiToolRequest.from_json(json)
# print the JSON string representation of the object
print ApiToolRequest.to_json()

# convert the object into a dict
api_tool_request_dict = api_tool_request_instance.to_dict()
# create an instance of ApiToolRequest from a dict
api_tool_request_form_dict = api_tool_request.from_dict(api_tool_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


