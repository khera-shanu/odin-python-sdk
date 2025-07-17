# ModelUpdate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**model_name** | **object** |  | 
**api_url** | **object** |  | 
**api_type** | **object** |  | 
**max_input_tokens** | [**MaxInputTokens**](MaxInputTokens.md) |  | 
**max_response_tokens** | [**MaxResponseTokens**](MaxResponseTokens.md) |  | 
**display_name** | **object** |  | 
**cost** | **object** |  | 
**hidden** | [**Hidden**](Hidden.md) |  | [optional] 
**api_key** | [**ApiKey**](ApiKey.md) |  | [optional] 
**api_version** | [**ApiVersion**](ApiVersion.md) |  | [optional] 
**is_default** | [**IsDefault**](IsDefault.md) |  | [optional] 
**is_default_extraction_model** | [**IsDefaultExtractionModel**](IsDefaultExtractionModel.md) |  | [optional] 
**is_default_citation_model** | [**IsDefaultCitationModel**](IsDefaultCitationModel.md) |  | [optional] 
**model_extra_params** | [**ModelExtraParams1**](ModelExtraParams1.md) |  | [optional] 

## Example

```python
from odin_sdk.models.model_update import ModelUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of ModelUpdate from a JSON string
model_update_instance = ModelUpdate.from_json(json)
# print the JSON string representation of the object
print ModelUpdate.to_json()

# convert the object into a dict
model_update_dict = model_update_instance.to_dict()
# create an instance of ModelUpdate from a dict
model_update_form_dict = model_update.from_dict(model_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


