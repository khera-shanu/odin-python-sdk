# WorkerInfoModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hostname** | **object** |  | 
**status** | **object** |  | 
**active_tasks** | **object** |  | [optional] 
**scheduled_tasks** | **object** |  | [optional] 
**reserved_tasks** | **object** |  | [optional] 
**processed** | [**Processed**](Processed.md) |  | [optional] 
**stats** | [**Stats**](Stats.md) |  | [optional] 

## Example

```python
from odin_sdk.models.worker_info_model import WorkerInfoModel

# TODO update the JSON string below
json = "{}"
# create an instance of WorkerInfoModel from a JSON string
worker_info_model_instance = WorkerInfoModel.from_json(json)
# print the JSON string representation of the object
print WorkerInfoModel.to_json()

# convert the object into a dict
worker_info_model_dict = worker_info_model_instance.to_dict()
# create an instance of WorkerInfoModel from a dict
worker_info_model_form_dict = worker_info_model.from_dict(worker_info_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


