# Role


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **object** |  | 
**name** | **object** |  | 
**created_by** | [**CreatedBy**](CreatedBy.md) |  | [optional] 
**created_at** | [**CreatedAt**](CreatedAt.md) |  | [optional] 
**updated_at** | [**UpdatedAt**](UpdatedAt.md) |  | [optional] 
**number_of_members** | **object** |  | 
**actions** | [**Actions**](Actions.md) |  | [optional] 
**sanitized_name** | [**SanitizedName**](SanitizedName.md) |  | [optional] 
**members** | [**Members2**](Members2.md) |  | [optional] 

## Example

```python
from odin_sdk.models.role import Role

# TODO update the JSON string below
json = "{}"
# create an instance of Role from a JSON string
role_instance = Role.from_json(json)
# print the JSON string representation of the object
print Role.to_json()

# convert the object into a dict
role_dict = role_instance.to_dict()
# create an instance of Role from a dict
role_form_dict = role.from_dict(role_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


