# APIKey


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**openai** | [**Openai**](Openai.md) |  | [optional] 
**anthropic** | [**Anthropic**](Anthropic.md) |  | [optional] 

## Example

```python
from odin_sdk.models.api_key import APIKey

# TODO update the JSON string below
json = "{}"
# create an instance of APIKey from a JSON string
api_key_instance = APIKey.from_json(json)
# print the JSON string representation of the object
print APIKey.to_json()

# convert the object into a dict
api_key_dict = api_key_instance.to_dict()
# create an instance of APIKey from a dict
api_key_form_dict = api_key.from_dict(api_key_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


