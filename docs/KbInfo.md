# KbInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**word_count** | [**WordCount**](WordCount.md) |  | [optional] 
**char_count** | [**CharCount**](CharCount.md) |  | [optional] 
**disk_usage** | [**DiskUsage**](DiskUsage.md) |  | [optional] 
**url** | [**Url**](Url.md) |  | [optional] 

## Example

```python
from odin_sdk.models.kb_info import KbInfo

# TODO update the JSON string below
json = "{}"
# create an instance of KbInfo from a JSON string
kb_info_instance = KbInfo.from_json(json)
# print the JSON string representation of the object
print KbInfo.to_json()

# convert the object into a dict
kb_info_dict = kb_info_instance.to_dict()
# create an instance of KbInfo from a dict
kb_info_form_dict = kb_info.from_dict(kb_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


