# DeleteJsonResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **object** |  | 
**json_id** | **object** |  | 

## Example

```python
from odin_sdk.models.delete_json_response import DeleteJsonResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteJsonResponse from a JSON string
delete_json_response_instance = DeleteJsonResponse.from_json(json)
# print the JSON string representation of the object
print DeleteJsonResponse.to_json()

# convert the object into a dict
delete_json_response_dict = delete_json_response_instance.to_dict()
# create an instance of DeleteJsonResponse from a dict
delete_json_response_form_dict = delete_json_response.from_dict(delete_json_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


