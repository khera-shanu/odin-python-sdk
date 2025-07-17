# ProjectInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **object** |  | 
**created_at** | **object** |  | 
**members** | **object** |  | 
**owner** | **object** |  | 
**description** | **object** |  | 
**type** | **object** |  | 
**model_name** | **object** |  | 
**system_prompt** | [**ProjectInfoSystemPrompt**](ProjectInfoSystemPrompt.md) |  | [optional] 
**id** | **object** |  | 

## Example

```python
from odin_sdk.models.project_info import ProjectInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectInfo from a JSON string
project_info_instance = ProjectInfo.from_json(json)
# print the JSON string representation of the object
print ProjectInfo.to_json()

# convert the object into a dict
project_info_dict = project_info_instance.to_dict()
# create an instance of ProjectInfo from a dict
project_info_form_dict = project_info.from_dict(project_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


