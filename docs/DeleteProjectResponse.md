# DeleteProjectResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **object** |  | 
**project_id** | **object** |  | 

## Example

```python
from odin_sdk.models.delete_project_response import DeleteProjectResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteProjectResponse from a JSON string
delete_project_response_instance = DeleteProjectResponse.from_json(json)
# print the JSON string representation of the object
print DeleteProjectResponse.to_json()

# convert the object into a dict
delete_project_response_dict = delete_project_response_instance.to_dict()
# create an instance of DeleteProjectResponse from a dict
delete_project_response_form_dict = delete_project_response.from_dict(delete_project_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


