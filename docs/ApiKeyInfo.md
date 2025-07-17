# ApiKeyInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **object** |  | 
**key_name** | [**KeyName**](KeyName.md) |  | [optional] 
**created_at** | [**CreatedAt**](CreatedAt.md) |  | [optional] 
**created_at_human_readable** | [**CreatedAtHumanReadable**](CreatedAtHumanReadable.md) |  | [optional] 

## Example

```python
from odin_sdk.models.api_key_info import ApiKeyInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ApiKeyInfo from a JSON string
api_key_info_instance = ApiKeyInfo.from_json(json)
# print the JSON string representation of the object
print ApiKeyInfo.to_json()

# convert the object into a dict
api_key_info_dict = api_key_info_instance.to_dict()
# create an instance of ApiKeyInfo from a dict
api_key_info_form_dict = api_key_info.from_dict(api_key_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


