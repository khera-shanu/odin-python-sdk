# MetricsResponse

Response model for metrics endpoint.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tools** | [**ToolMetrics**](ToolMetrics.md) |  | 
**token_usage** | [**TokenUsage**](TokenUsage.md) |  | 

## Example

```python
from odin_sdk.models.metrics_response import MetricsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of MetricsResponse from a JSON string
metrics_response_instance = MetricsResponse.from_json(json)
# print the JSON string representation of the object
print MetricsResponse.to_json()

# convert the object into a dict
metrics_response_dict = metrics_response_instance.to_dict()
# create an instance of MetricsResponse from a dict
metrics_response_form_dict = metrics_response.from_dict(metrics_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


