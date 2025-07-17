# FolderExternalLinkInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | **object** |  | 
**path** | **object** |  | 
**type** | **object** |  | 
**url** | **object** |  | 
**metadata** | **object** |  | 
**uploader** | **object** |  | 

## Example

```python
from odin_sdk.models.folder_external_link_info import FolderExternalLinkInfo

# TODO update the JSON string below
json = "{}"
# create an instance of FolderExternalLinkInfo from a JSON string
folder_external_link_info_instance = FolderExternalLinkInfo.from_json(json)
# print the JSON string representation of the object
print FolderExternalLinkInfo.to_json()

# convert the object into a dict
folder_external_link_info_dict = folder_external_link_info_instance.to_dict()
# create an instance of FolderExternalLinkInfo from a dict
folder_external_link_info_form_dict = folder_external_link_info.from_dict(folder_external_link_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


