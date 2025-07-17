# ProjectApiKeys


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**openai** | [**Openai**](Openai.md) |  | [optional] 
**anthropic** | [**Anthropic**](Anthropic.md) |  | [optional] 

## Example

```python
from odin_sdk.models.project_api_keys import ProjectApiKeys

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectApiKeys from a JSON string
project_api_keys_instance = ProjectApiKeys.from_json(json)
# print the JSON string representation of the object
print ProjectApiKeys.to_json()

# convert the object into a dict
project_api_keys_dict = project_api_keys_instance.to_dict()
# create an instance of ProjectApiKeys from a dict
project_api_keys_form_dict = project_api_keys.from_dict(project_api_keys_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


