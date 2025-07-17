# ModelCreate


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
**model_id** | **object** |  | 

## Example

```python
from odin_sdk.models.model_create import ModelCreate

# TODO update the JSON string below
json = "{}"
# create an instance of ModelCreate from a JSON string
model_create_instance = ModelCreate.from_json(json)
# print the JSON string representation of the object
print ModelCreate.to_json()

# convert the object into a dict
model_create_dict = model_create_instance.to_dict()
# create an instance of ModelCreate from a dict
model_create_form_dict = model_create.from_dict(model_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


