# AsanaIntegration


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uid** | **object** |  | 
**asana_email** | **object** |  | 
**asana_user_id** | [**AsanaUserId**](AsanaUserId.md) |  | [optional] 

## Example

```python
from odin_sdk.models.asana_integration import AsanaIntegration

# TODO update the JSON string below
json = "{}"
# create an instance of AsanaIntegration from a JSON string
asana_integration_instance = AsanaIntegration.from_json(json)
# print the JSON string representation of the object
print AsanaIntegration.to_json()

# convert the object into a dict
asana_integration_dict = asana_integration_instance.to_dict()
# create an instance of AsanaIntegration from a dict
asana_integration_form_dict = asana_integration.from_dict(asana_integration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


