# DeleteUserRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | **object** |  | 
**user_id** | **object** |  | 

## Example

```python
from odin_sdk.models.delete_user_request import DeleteUserRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteUserRequest from a JSON string
delete_user_request_instance = DeleteUserRequest.from_json(json)
# print the JSON string representation of the object
print DeleteUserRequest.to_json()

# convert the object into a dict
delete_user_request_dict = delete_user_request_instance.to_dict()
# create an instance of DeleteUserRequest from a dict
delete_user_request_form_dict = delete_user_request.from_dict(delete_user_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


