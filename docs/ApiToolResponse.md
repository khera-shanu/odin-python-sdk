# ApiToolResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **object** | Whether the API request was successful | 
**message** | **object** | A message describing the result | 
**response** | [**Response**](Response.md) |  | [optional] 

## Example

```python
from odin_sdk.models.api_tool_response import ApiToolResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ApiToolResponse from a JSON string
api_tool_response_instance = ApiToolResponse.from_json(json)
# print the JSON string representation of the object
print ApiToolResponse.to_json()

# convert the object into a dict
api_tool_response_dict = api_tool_response_instance.to_dict()
# create an instance of ApiToolResponse from a dict
api_tool_response_form_dict = api_tool_response.from_dict(api_tool_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


