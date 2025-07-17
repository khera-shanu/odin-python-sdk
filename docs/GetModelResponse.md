# GetModelResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **object** |  | 
**model_name** | **object** |  | 
**api_url** | **object** |  | 
**api_key** | **object** |  | 
**api_type** | **object** |  | 
**max_response_tokens** | **object** |  | 
**max_input_tokens** | **object** |  | [optional] 
**api_provider** | **object** |  | 
**model_extra_params** | [**ModelExtraParams**](ModelExtraParams.md) |  | [optional] 
**api_version** | [**ApiVersion**](ApiVersion.md) |  | [optional] 

## Example

```python
from odin_sdk.models.get_model_response import GetModelResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetModelResponse from a JSON string
get_model_response_instance = GetModelResponse.from_json(json)
# print the JSON string representation of the object
print GetModelResponse.to_json()

# convert the object into a dict
get_model_response_dict = get_model_response_instance.to_dict()
# create an instance of GetModelResponse from a dict
get_model_response_form_dict = get_model_response.from_dict(get_model_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


