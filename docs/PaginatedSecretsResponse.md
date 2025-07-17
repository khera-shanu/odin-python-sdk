# PaginatedSecretsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**secrets** | **object** |  | 
**total** | **object** |  | 
**page** | **object** |  | 
**limit** | **object** |  | 
**total_pages** | **object** |  | 

## Example

```python
from odin_sdk.models.paginated_secrets_response import PaginatedSecretsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedSecretsResponse from a JSON string
paginated_secrets_response_instance = PaginatedSecretsResponse.from_json(json)
# print the JSON string representation of the object
print PaginatedSecretsResponse.to_json()

# convert the object into a dict
paginated_secrets_response_dict = paginated_secrets_response_instance.to_dict()
# create an instance of PaginatedSecretsResponse from a dict
paginated_secrets_response_form_dict = paginated_secrets_response.from_dict(paginated_secrets_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


