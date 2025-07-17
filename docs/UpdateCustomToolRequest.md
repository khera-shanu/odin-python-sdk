# UpdateCustomToolRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | [**Name2**](Name2.md) |  | [optional] 
**description** | [**Description5**](Description5.md) |  | [optional] 
**inputs** | [**Inputs**](Inputs.md) |  | [optional] 
**steps** | [**Steps**](Steps.md) |  | [optional] 
**is_public** | [**IsPublic1**](IsPublic1.md) |  | [optional] 

## Example

```python
from odin_sdk.models.update_custom_tool_request import UpdateCustomToolRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateCustomToolRequest from a JSON string
update_custom_tool_request_instance = UpdateCustomToolRequest.from_json(json)
# print the JSON string representation of the object
print UpdateCustomToolRequest.to_json()

# convert the object into a dict
update_custom_tool_request_dict = update_custom_tool_request_instance.to_dict()
# create an instance of UpdateCustomToolRequest from a dict
update_custom_tool_request_form_dict = update_custom_tool_request.from_dict(update_custom_tool_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


