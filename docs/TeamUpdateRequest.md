# TeamUpdateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | [**Name**](Name.md) |  | [optional] 
**allowed_seats** | [**AllowedSeats1**](AllowedSeats1.md) |  | [optional] 
**active** | [**Active1**](Active1.md) |  | [optional] 
**settings** | [**Settings1**](Settings1.md) |  | [optional] 

## Example

```python
from odin_sdk.models.team_update_request import TeamUpdateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TeamUpdateRequest from a JSON string
team_update_request_instance = TeamUpdateRequest.from_json(json)
# print the JSON string representation of the object
print TeamUpdateRequest.to_json()

# convert the object into a dict
team_update_request_dict = team_update_request_instance.to_dict()
# create an instance of TeamUpdateRequest from a dict
team_update_request_form_dict = team_update_request.from_dict(team_update_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


