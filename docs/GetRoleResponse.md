# GetRoleResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **object** |  | 
**rules** | [**Rules**](Rules.md) |  | 

## Example

```python
from odin_sdk.models.get_role_response import GetRoleResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetRoleResponse from a JSON string
get_role_response_instance = GetRoleResponse.from_json(json)
# print the JSON string representation of the object
print GetRoleResponse.to_json()

# convert the object into a dict
get_role_response_dict = get_role_response_instance.to_dict()
# create an instance of GetRoleResponse from a dict
get_role_response_form_dict = get_role_response.from_dict(get_role_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


