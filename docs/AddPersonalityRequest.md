# AddPersonalityRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **object** |  | 
**instructions** | **object** |  | 
**type** | **object** |  | 
**project_id** | **object** |  | 
**temperature** | **object** |  | 

## Example

```python
from odin_sdk.models.add_personality_request import AddPersonalityRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AddPersonalityRequest from a JSON string
add_personality_request_instance = AddPersonalityRequest.from_json(json)
# print the JSON string representation of the object
print AddPersonalityRequest.to_json()

# convert the object into a dict
add_personality_request_dict = add_personality_request_instance.to_dict()
# create an instance of AddPersonalityRequest from a dict
add_personality_request_form_dict = add_personality_request.from_dict(add_personality_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


