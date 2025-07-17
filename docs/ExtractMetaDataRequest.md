# ExtractMetaDataRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**text** | **object** | Text to extract information from. | 
**example_json** | **object** | Information to extract from the text along with python datatypes. | 
**model** | **object** | Model to use for the extraction. Defaults to gpt-4o-mini. | [optional] 
**temperature** | **object** | Temperature to use for the extraction. Defaults to 0.0. | [optional] 

## Example

```python
from odin_sdk.models.extract_meta_data_request import ExtractMetaDataRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ExtractMetaDataRequest from a JSON string
extract_meta_data_request_instance = ExtractMetaDataRequest.from_json(json)
# print the JSON string representation of the object
print ExtractMetaDataRequest.to_json()

# convert the object into a dict
extract_meta_data_request_dict = extract_meta_data_request_instance.to_dict()
# create an instance of ExtractMetaDataRequest from a dict
extract_meta_data_request_form_dict = extract_meta_data_request.from_dict(extract_meta_data_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


