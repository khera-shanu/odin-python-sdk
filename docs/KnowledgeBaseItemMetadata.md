# KnowledgeBaseItemMetadata

Metadata of the document

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**file_name** | [**FileName**](FileName.md) |  | [optional] 
**doc_type** | [**DocType1**](DocType1.md) |  | [optional] 
**added_by** | [**AddedBy**](AddedBy.md) |  | [optional] 
**word_count** | [**WordCount1**](WordCount1.md) |  | [optional] 
**char_count** | [**CharCount1**](CharCount1.md) |  | [optional] 
**disk_usage** | [**DiskUsage1**](DiskUsage1.md) |  | [optional] 
**custom_metadata** | [**CustomMetadata**](CustomMetadata.md) |  | [optional] 

## Example

```python
from odin_sdk.models.knowledge_base_item_metadata import KnowledgeBaseItemMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of KnowledgeBaseItemMetadata from a JSON string
knowledge_base_item_metadata_instance = KnowledgeBaseItemMetadata.from_json(json)
# print the JSON string representation of the object
print KnowledgeBaseItemMetadata.to_json()

# convert the object into a dict
knowledge_base_item_metadata_dict = knowledge_base_item_metadata_instance.to_dict()
# create an instance of KnowledgeBaseItemMetadata from a dict
knowledge_base_item_metadata_form_dict = knowledge_base_item_metadata.from_dict(knowledge_base_item_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


