# TranslateTextsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **object** |  | 
**translated_texts** | **object** |  | 

## Example

```python
from odin_sdk.models.translate_texts_response import TranslateTextsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TranslateTextsResponse from a JSON string
translate_texts_response_instance = TranslateTextsResponse.from_json(json)
# print the JSON string representation of the object
print TranslateTextsResponse.to_json()

# convert the object into a dict
translate_texts_response_dict = translate_texts_response_instance.to_dict()
# create an instance of TranslateTextsResponse from a dict
translate_texts_response_form_dict = translate_texts_response.from_dict(translate_texts_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


