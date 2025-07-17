# ContentSpinnerRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**input_text** | **object** | Input text to create content from. | 
**project_id** | **object** | Project ID in which to run the spinner. | 
**additional_instructions** | [**AdditionalInstructions**](AdditionalInstructions.md) |  | [optional] 
**temperature** | [**Temperature**](Temperature.md) |  | [optional] 
**model_name** | [**ModelName1**](ModelName1.md) |  | [optional] 

## Example

```python
from odin_sdk.models.content_spinner_request import ContentSpinnerRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ContentSpinnerRequest from a JSON string
content_spinner_request_instance = ContentSpinnerRequest.from_json(json)
# print the JSON string representation of the object
print ContentSpinnerRequest.to_json()

# convert the object into a dict
content_spinner_request_dict = content_spinner_request_instance.to_dict()
# create an instance of ContentSpinnerRequest from a dict
content_spinner_request_form_dict = content_spinner_request.from_dict(content_spinner_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


