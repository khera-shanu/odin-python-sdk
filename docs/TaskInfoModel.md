# TaskInfoModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**task_id** | **object** |  | 
**task_name** | **object** |  | 
**status** | **object** |  | 
**project_id** | [**ProjectId**](ProjectId.md) |  | [optional] 
**started_at** | [**StartedAt1**](StartedAt1.md) |  | [optional] 
**completed_at** | [**CompletedAt1**](CompletedAt1.md) |  | [optional] 
**duration_seconds** | [**DurationSeconds**](DurationSeconds.md) |  | [optional] 
**args** | [**Args**](Args.md) |  | [optional] 
**kwargs** | [**Kwargs**](Kwargs.md) |  | [optional] 
**result** | [**Result**](Result.md) |  | [optional] 
**traceback** | [**Traceback**](Traceback.md) |  | [optional] 
**worker** | [**Worker**](Worker.md) |  | [optional] 
**retries** | [**Retries**](Retries.md) |  | [optional] 

## Example

```python
from odin_sdk.models.task_info_model import TaskInfoModel

# TODO update the JSON string below
json = "{}"
# create an instance of TaskInfoModel from a JSON string
task_info_model_instance = TaskInfoModel.from_json(json)
# print the JSON string representation of the object
print TaskInfoModel.to_json()

# convert the object into a dict
task_info_model_dict = task_info_model_instance.to_dict()
# create an instance of TaskInfoModel from a dict
task_info_model_form_dict = task_info_model.from_dict(task_info_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


