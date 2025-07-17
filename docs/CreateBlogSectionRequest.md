# CreateBlogSectionRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**keywords** | **object** |  | 
**initial_blog_content** | **object** |  | 
**retries** | **object** |  | [optional] 

## Example

```python
from odin_sdk.models.create_blog_section_request import CreateBlogSectionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateBlogSectionRequest from a JSON string
create_blog_section_request_instance = CreateBlogSectionRequest.from_json(json)
# print the JSON string representation of the object
print CreateBlogSectionRequest.to_json()

# convert the object into a dict
create_blog_section_request_dict = create_blog_section_request_instance.to_dict()
# create an instance of CreateBlogSectionRequest from a dict
create_blog_section_request_form_dict = create_blog_section_request.from_dict(create_blog_section_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


