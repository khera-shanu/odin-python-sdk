# ToolMetrics

Model for tool usage metrics.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tool_calls_total** | **object** |  | 
**tool_calls_responses** | **object** |  | 
**tool_calls_successful** | **object** |  | 
**tool_calls_failures** | **object** |  | 

## Example

```python
from odin_sdk.models.tool_metrics import ToolMetrics

# TODO update the JSON string below
json = "{}"
# create an instance of ToolMetrics from a JSON string
tool_metrics_instance = ToolMetrics.from_json(json)
# print the JSON string representation of the object
print ToolMetrics.to_json()

# convert the object into a dict
tool_metrics_dict = tool_metrics_instance.to_dict()
# create an instance of ToolMetrics from a dict
tool_metrics_form_dict = tool_metrics.from_dict(tool_metrics_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


