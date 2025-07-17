# GetKBPageResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**docs** | **object** |  | 
**folders** | [**Folders**](Folders.md) |  | [optional] 
**kb_info** | [**GetKBPageResponseKbInfo**](GetKBPageResponseKbInfo.md) |  | [optional] 

## Example

```python
from odin_sdk.models.get_kb_page_response import GetKBPageResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetKBPageResponse from a JSON string
get_kb_page_response_instance = GetKBPageResponse.from_json(json)
# print the JSON string representation of the object
print GetKBPageResponse.to_json()

# convert the object into a dict
get_kb_page_response_dict = get_kb_page_response_instance.to_dict()
# create an instance of GetKBPageResponse from a dict
get_kb_page_response_form_dict = get_kb_page_response.from_dict(get_kb_page_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


