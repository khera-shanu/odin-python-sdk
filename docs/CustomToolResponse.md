# CustomToolResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **object** | Unique identifier for the custom tool | 
**name** | **object** | Name of the custom tool | 
**description** | [**Description5**](Description5.md) |  | [optional] 
**inputs** | [**Dict[str, ToolInput]**](ToolInput.md) | Tool inputs configuration | 
**steps** | [**Dict[str, ToolStep]**](ToolStep.md) | Tool steps configuration | 
**test_step_results** | **object** | Test step execution results | [optional] 
**project_id** | **object** | Project ID this tool belongs to | 
**created_by** | **object** | User ID who created this tool | 
**created_at** | **object** | Creation timestamp | 
**updated_at** | **object** | Last update timestamp | 
**is_published** | **object** | Whether this tool is published | 
**version** | [**Version1**](Version1.md) |  | [optional] 
**published_at** | [**PublishedAt1**](PublishedAt1.md) |  | [optional] 
**is_draft** | **object** | Whether this tool has unsaved draft changes | 
**is_public** | **object** | Whether this tool is publicly available to all users | 

## Example

```python
from odin_sdk.models.custom_tool_response import CustomToolResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CustomToolResponse from a JSON string
custom_tool_response_instance = CustomToolResponse.from_json(json)
# print the JSON string representation of the object
print CustomToolResponse.to_json()

# convert the object into a dict
custom_tool_response_dict = custom_tool_response_instance.to_dict()
# create an instance of CustomToolResponse from a dict
custom_tool_response_form_dict = custom_tool_response.from_dict(custom_tool_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


