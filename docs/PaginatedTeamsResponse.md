# PaginatedTeamsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total** | **object** |  | 
**teams** | **object** |  | 

## Example

```python
from odin_sdk.models.paginated_teams_response import PaginatedTeamsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedTeamsResponse from a JSON string
paginated_teams_response_instance = PaginatedTeamsResponse.from_json(json)
# print the JSON string representation of the object
print PaginatedTeamsResponse.to_json()

# convert the object into a dict
paginated_teams_response_dict = paginated_teams_response_instance.to_dict()
# create an instance of PaginatedTeamsResponse from a dict
paginated_teams_response_form_dict = paginated_teams_response.from_dict(paginated_teams_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


