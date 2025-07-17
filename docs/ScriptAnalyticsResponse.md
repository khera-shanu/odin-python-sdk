# ScriptAnalyticsResponse

Response model for script analytics

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**script_id** | **object** |  | 
**script_name** | **object** |  | 
**runtime** | **object** |  | 
**total_executions** | **object** |  | 
**successful_executions** | **object** |  | 
**failed_executions** | **object** |  | 
**timeout_executions** | **object** |  | 
**success_rate** | **object** |  | 
**avg_success_time_ms** | [**AvgSuccessTimeMs**](AvgSuccessTimeMs.md) |  | 
**min_success_time_ms** | [**MinSuccessTimeMs**](MinSuccessTimeMs.md) |  | 
**max_success_time_ms** | [**MaxSuccessTimeMs**](MaxSuccessTimeMs.md) |  | 
**avg_memory_used_mb** | [**AvgMemoryUsedMb**](AvgMemoryUsedMb.md) |  | 
**last_executed_at** | [**LastExecutedAt**](LastExecutedAt.md) |  | 
**first_executed_at** | [**FirstExecutedAt**](FirstExecutedAt.md) |  | 

## Example

```python
from odin_sdk.models.script_analytics_response import ScriptAnalyticsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ScriptAnalyticsResponse from a JSON string
script_analytics_response_instance = ScriptAnalyticsResponse.from_json(json)
# print the JSON string representation of the object
print ScriptAnalyticsResponse.to_json()

# convert the object into a dict
script_analytics_response_dict = script_analytics_response_instance.to_dict()
# create an instance of ScriptAnalyticsResponse from a dict
script_analytics_response_form_dict = script_analytics_response.from_dict(script_analytics_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


