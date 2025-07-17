# KnowledgeBaseItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**upload_date** | [**UploadDate**](UploadDate.md) |  | [optional] 
**doc_type** | [**DocType1**](DocType1.md) |  | [optional] 
**url** | [**Url1**](Url1.md) |  | [optional] 
**status** | [**Status4**](Status4.md) |  | [optional] 
**metadata** | [**KnowledgeBaseItemMetadata**](KnowledgeBaseItemMetadata.md) |  | [optional] 

## Example

```python
from odin_sdk.models.knowledge_base_item import KnowledgeBaseItem

# TODO update the JSON string below
json = "{}"
# create an instance of KnowledgeBaseItem from a JSON string
knowledge_base_item_instance = KnowledgeBaseItem.from_json(json)
# print the JSON string representation of the object
print KnowledgeBaseItem.to_json()

# convert the object into a dict
knowledge_base_item_dict = knowledge_base_item_instance.to_dict()
# create an instance of KnowledgeBaseItem from a dict
knowledge_base_item_form_dict = knowledge_base_item.from_dict(knowledge_base_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


