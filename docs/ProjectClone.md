# ProjectClone


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**original_project_id** | **object** |  | 
**new_project_name** | **object** |  | 
**target_user_id** | **object** |  | 

## Example

```python
from odin_sdk.models.project_clone import ProjectClone

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectClone from a JSON string
project_clone_instance = ProjectClone.from_json(json)
# print the JSON string representation of the object
print ProjectClone.to_json()

# convert the object into a dict
project_clone_dict = project_clone_instance.to_dict()
# create an instance of ProjectClone from a dict
project_clone_form_dict = project_clone.from_dict(project_clone_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


