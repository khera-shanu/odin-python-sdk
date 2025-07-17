# SecretCreate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **object** |  | 
**value** | **object** |  | 
**label** | [**Label1**](Label1.md) |  | [optional] 
**description** | [**Description1**](Description1.md) |  | [optional] 

## Example

```python
from odin_sdk.models.secret_create import SecretCreate

# TODO update the JSON string below
json = "{}"
# create an instance of SecretCreate from a JSON string
secret_create_instance = SecretCreate.from_json(json)
# print the JSON string representation of the object
print SecretCreate.to_json()

# convert the object into a dict
secret_create_dict = secret_create_instance.to_dict()
# create an instance of SecretCreate from a dict
secret_create_form_dict = secret_create.from_dict(secret_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


