# GetKBPageResponseKbInfo

Knowledge base information

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**word_count** | [**WordCount**](WordCount.md) |  | [optional] 
**char_count** | [**CharCount**](CharCount.md) |  | [optional] 
**disk_usage** | [**DiskUsage**](DiskUsage.md) |  | [optional] 
**url** | [**Url**](Url.md) |  | [optional] 

## Example

```python
from odin_sdk.models.get_kb_page_response_kb_info import GetKBPageResponseKbInfo

# TODO update the JSON string below
json = "{}"
# create an instance of GetKBPageResponseKbInfo from a JSON string
get_kb_page_response_kb_info_instance = GetKBPageResponseKbInfo.from_json(json)
# print the JSON string representation of the object
print GetKBPageResponseKbInfo.to_json()

# convert the object into a dict
get_kb_page_response_kb_info_dict = get_kb_page_response_kb_info_instance.to_dict()
# create an instance of GetKBPageResponseKbInfo from a dict
get_kb_page_response_kb_info_form_dict = get_kb_page_response_kb_info.from_dict(get_kb_page_response_kb_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


