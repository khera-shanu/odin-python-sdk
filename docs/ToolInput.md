# ToolInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | [**Id3**](Id3.md) |  | [optional] 
**type** | **object** | The input type (string, number, boolean, etc.) | 
**value** | **object** | The input value or description | 
**manual_input** | **object** | Whether this is manual input or agent controlled | [optional] 
**description** | [**Description11**](Description11.md) |  | [optional] 

## Example

```python
from odin_sdk.models.tool_input import ToolInput

# TODO update the JSON string below
json = "{}"
# create an instance of ToolInput from a JSON string
tool_input_instance = ToolInput.from_json(json)
# print the JSON string representation of the object
print ToolInput.to_json()

# convert the object into a dict
tool_input_dict = tool_input_instance.to_dict()
# create an instance of ToolInput from a dict
tool_input_form_dict = tool_input.from_dict(tool_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


