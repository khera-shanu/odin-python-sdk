# TagRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | **object** |  | 
**document_id** | **object** |  | 
**tags** | **object** |  | 

## Example

```python
from odin_sdk.models.tag_request import TagRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TagRequest from a JSON string
tag_request_instance = TagRequest.from_json(json)
# print the JSON string representation of the object
print TagRequest.to_json()

# convert the object into a dict
tag_request_dict = tag_request_instance.to_dict()
# create an instance of TagRequest from a dict
tag_request_form_dict = tag_request.from_dict(tag_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


