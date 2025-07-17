# ProjectKbInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**word_count** | [**WordCount**](WordCount.md) |  | [optional] 
**char_count** | [**CharCount**](CharCount.md) |  | [optional] 
**disk_usage** | [**DiskUsage**](DiskUsage.md) |  | [optional] 
**url** | [**Url**](Url.md) |  | [optional] 

## Example

```python
from odin_sdk.models.project_kb_info import ProjectKbInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectKbInfo from a JSON string
project_kb_info_instance = ProjectKbInfo.from_json(json)
# print the JSON string representation of the object
print ProjectKbInfo.to_json()

# convert the object into a dict
project_kb_info_dict = project_kb_info_instance.to_dict()
# create an instance of ProjectKbInfo from a dict
project_kb_info_form_dict = project_kb_info.from_dict(project_kb_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


