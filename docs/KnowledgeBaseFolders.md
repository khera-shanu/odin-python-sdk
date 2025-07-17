# KnowledgeBaseFolders


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **object** |  | 
**path** | **object** |  | 
**size** | [**Size**](Size.md) |  | 
**type** | **object** |  | 
**id** | **object** |  | 
**last_updated** | [**LastUpdated**](LastUpdated.md) |  | 
**external_link_info** | [**KnowledgeBaseFoldersExternalLinkInfo**](KnowledgeBaseFoldersExternalLinkInfo.md) |  | [optional] 

## Example

```python
from odin_sdk.models.knowledge_base_folders import KnowledgeBaseFolders

# TODO update the JSON string below
json = "{}"
# create an instance of KnowledgeBaseFolders from a JSON string
knowledge_base_folders_instance = KnowledgeBaseFolders.from_json(json)
# print the JSON string representation of the object
print KnowledgeBaseFolders.to_json()

# convert the object into a dict
knowledge_base_folders_dict = knowledge_base_folders_instance.to_dict()
# create an instance of KnowledgeBaseFolders from a dict
knowledge_base_folders_form_dict = knowledge_base_folders.from_dict(knowledge_base_folders_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


