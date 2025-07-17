# HTMLContentRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**content** | **object** |  | 
**project_id** | **object** |  | 
**metadata** | [**Metadata2**](Metadata2.md) |  | [optional] 
**file_type** | [**FileType1**](FileType1.md) |  | [optional] 
**force** | [**Force**](Force.md) |  | [optional] 
**is_quick_upload** | [**IsQuickUpload**](IsQuickUpload.md) |  | [optional] 
**pageurl** | **object** |  | 
**path** | [**Path**](Path.md) |  | [optional] 

## Example

```python
from odin_sdk.models.html_content_request import HTMLContentRequest

# TODO update the JSON string below
json = "{}"
# create an instance of HTMLContentRequest from a JSON string
html_content_request_instance = HTMLContentRequest.from_json(json)
# print the JSON string representation of the object
print HTMLContentRequest.to_json()

# convert the object into a dict
html_content_request_dict = html_content_request_instance.to_dict()
# create an instance of HTMLContentRequest from a dict
html_content_request_form_dict = html_content_request.from_dict(html_content_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


