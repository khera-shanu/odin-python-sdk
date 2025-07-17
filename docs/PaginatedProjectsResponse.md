# PaginatedProjectsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total** | **object** |  | 
**projects** | **object** |  | 

## Example

```python
from odin_sdk.models.paginated_projects_response import PaginatedProjectsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedProjectsResponse from a JSON string
paginated_projects_response_instance = PaginatedProjectsResponse.from_json(json)
# print the JSON string representation of the object
print PaginatedProjectsResponse.to_json()

# convert the object into a dict
paginated_projects_response_dict = paginated_projects_response_instance.to_dict()
# create an instance of PaginatedProjectsResponse from a dict
paginated_projects_response_form_dict = paginated_projects_response.from_dict(paginated_projects_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


