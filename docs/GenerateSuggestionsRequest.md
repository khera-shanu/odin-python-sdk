# GenerateSuggestionsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**messages** | **object** |  | 
**no_of_suggestions** | **object** |  | 
**conversation_type** | **object** |  | 
**project_id** | **object** |  | 
**chat_id** | **object** |  | 
**model_name** | **object** |  | [optional] 
**system_prompt** | [**SystemPrompt**](SystemPrompt.md) |  | [optional] 

## Example

```python
from odin_sdk.models.generate_suggestions_request import GenerateSuggestionsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GenerateSuggestionsRequest from a JSON string
generate_suggestions_request_instance = GenerateSuggestionsRequest.from_json(json)
# print the JSON string representation of the object
print GenerateSuggestionsRequest.to_json()

# convert the object into a dict
generate_suggestions_request_dict = generate_suggestions_request_instance.to_dict()
# create an instance of GenerateSuggestionsRequest from a dict
generate_suggestions_request_form_dict = generate_suggestions_request.from_dict(generate_suggestions_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


