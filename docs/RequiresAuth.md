# RequiresAuth

Whether the MCP requires authentication ('oauth', 'api_key', 'no')

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from odin_sdk.models.requires_auth import RequiresAuth

# TODO update the JSON string below
json = "{}"
# create an instance of RequiresAuth from a JSON string
requires_auth_instance = RequiresAuth.from_json(json)
# print the JSON string representation of the object
print RequiresAuth.to_json()

# convert the object into a dict
requires_auth_dict = requires_auth_instance.to_dict()
# create an instance of RequiresAuth from a dict
requires_auth_form_dict = requires_auth.from_dict(requires_auth_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


