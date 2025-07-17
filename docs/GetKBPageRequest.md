# GetKBPageRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**page** | **object** | The page number to retrieve | [optional] 
**items_per_page** | **object** | The number of items per page | [optional] 
**filters** | [**Filters2**](Filters2.md) |  | [optional] 
**name_search** | [**NameSearch**](NameSearch.md) |  | [optional] 
**content_keys** | [**ContentKeys**](ContentKeys.md) |  | [optional] 
**path** | [**Path1**](Path1.md) |  | [optional] 
**recursive** | **object** | Whether to retrieve subfolders | [optional] 

## Example

```python
from odin_sdk.models.get_kb_page_request import GetKBPageRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GetKBPageRequest from a JSON string
get_kb_page_request_instance = GetKBPageRequest.from_json(json)
# print the JSON string representation of the object
print GetKBPageRequest.to_json()

# convert the object into a dict
get_kb_page_request_dict = get_kb_page_request_instance.to_dict()
# create an instance of GetKBPageRequest from a dict
get_kb_page_request_form_dict = get_kb_page_request.from_dict(get_kb_page_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


