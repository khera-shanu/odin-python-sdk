# CreateProjectRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_name** | **object** |  | 
**project_description** | **object** |  | 
**project_type** | [**ProjectType**](ProjectType.md) |  | [optional] 
**personality_name** | [**PersonalityName**](PersonalityName.md) |  | [optional] 
**personality_instructions** | [**PersonalityInstructions**](PersonalityInstructions.md) |  | [optional] 
**personality_id** | [**PersonalityId1**](PersonalityId1.md) |  | [optional] 
**personality_type** | [**PersonalityType**](PersonalityType.md) |  | [optional] 
**personality_temperature** | [**PersonalityTemperature**](PersonalityTemperature.md) |  | [optional] 

## Example

```python
from odin_sdk.models.create_project_request import CreateProjectRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateProjectRequest from a JSON string
create_project_request_instance = CreateProjectRequest.from_json(json)
# print the JSON string representation of the object
print CreateProjectRequest.to_json()

# convert the object into a dict
create_project_request_dict = create_project_request_instance.to_dict()
# create an instance of CreateProjectRequest from a dict
create_project_request_form_dict = create_project_request.from_dict(create_project_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


