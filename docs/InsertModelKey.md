# InsertModelKey


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**model_name** | **object** |  | 
**api_url** | [**ApiUrl**](ApiUrl.md) |  | [optional] 
**api_key** | **object** |  | 
**api_type** | **object** |  | 
**max_response_tokens** | **object** |  | 
**max_input_tokens** | **object** |  | 
**model_extra_params** | [**ModelExtraParams**](ModelExtraParams.md) |  | [optional] 
**api_version** | [**ApiVersion**](ApiVersion.md) |  | [optional] 

## Example

```python
from odin_sdk.models.insert_model_key import InsertModelKey

# TODO update the JSON string below
json = "{}"
# create an instance of InsertModelKey from a JSON string
insert_model_key_instance = InsertModelKey.from_json(json)
# print the JSON string representation of the object
print InsertModelKey.to_json()

# convert the object into a dict
insert_model_key_dict = insert_model_key_instance.to_dict()
# create an instance of InsertModelKey from a dict
insert_model_key_form_dict = insert_model_key.from_dict(insert_model_key_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


