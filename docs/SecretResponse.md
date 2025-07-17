# SecretResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **object** |  | 
**key** | **object** |  | 
**value** | [**Value**](Value.md) |  | [optional] 
**label** | **object** |  | 
**description** | [**Description1**](Description1.md) |  | [optional] 
**created_by** | **object** |  | 
**creator_email** | [**CreatorEmail**](CreatorEmail.md) |  | [optional] 
**created_at** | **object** |  | 
**updated_at** | **object** |  | 
**is_deleted** | [**IsDeleted**](IsDeleted.md) |  | [optional] 
**is_encrypted** | [**IsEncrypted**](IsEncrypted.md) |  | [optional] 

## Example

```python
from odin_sdk.models.secret_response import SecretResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SecretResponse from a JSON string
secret_response_instance = SecretResponse.from_json(json)
# print the JSON string representation of the object
print SecretResponse.to_json()

# convert the object into a dict
secret_response_dict = secret_response_instance.to_dict()
# create an instance of SecretResponse from a dict
secret_response_form_dict = secret_response.from_dict(secret_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


