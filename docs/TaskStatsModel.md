# TaskStatsModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**task_name** | **object** |  | 
**total_executions** | **object** |  | 
**successful_executions** | **object** |  | 
**failed_executions** | **object** |  | 
**terminated_executions** | **object** |  | [optional] 
**avg_duration** | [**AvgDuration**](AvgDuration.md) |  | [optional] 
**median_duration** | [**MedianDuration**](MedianDuration.md) |  | [optional] 
**min_duration** | [**MinDuration**](MinDuration.md) |  | [optional] 
**max_duration** | [**MaxDuration**](MaxDuration.md) |  | [optional] 

## Example

```python
from odin_sdk.models.task_stats_model import TaskStatsModel

# TODO update the JSON string below
json = "{}"
# create an instance of TaskStatsModel from a JSON string
task_stats_model_instance = TaskStatsModel.from_json(json)
# print the JSON string representation of the object
print TaskStatsModel.to_json()

# convert the object into a dict
task_stats_model_dict = task_stats_model_instance.to_dict()
# create an instance of TaskStatsModel from a dict
task_stats_model_form_dict = task_stats_model.from_dict(task_stats_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


