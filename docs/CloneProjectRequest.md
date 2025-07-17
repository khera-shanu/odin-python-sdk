# CloneProjectRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | **object** |  | 
**new_project_name** | **object** |  | 

## Example

```python
from odin_sdk.models.clone_project_request import CloneProjectRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CloneProjectRequest from a JSON string
clone_project_request_instance = CloneProjectRequest.from_json(json)
# print the JSON string representation of the object
print CloneProjectRequest.to_json()

# convert the object into a dict
clone_project_request_dict = clone_project_request_instance.to_dict()
# create an instance of CloneProjectRequest from a dict
clone_project_request_form_dict = clone_project_request.from_dict(clone_project_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


