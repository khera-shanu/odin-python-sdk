# KnowledgeBasePageItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | [**Id2**](Id2.md) |  | [optional] 
**content_key** | [**ContentKey1**](ContentKey1.md) |  | [optional] 
**upload_date** | [**UploadDate**](UploadDate.md) |  | [optional] 
**doc_type** | [**DocType1**](DocType1.md) |  | [optional] 
**url** | [**Url1**](Url1.md) |  | [optional] 
**status** | [**Status4**](Status4.md) |  | [optional] 
**path** | [**Path2**](Path2.md) |  | [optional] 
**document_id** | [**DocumentId1**](DocumentId1.md) |  | [optional] 
**metadata** | [**Metadata3**](Metadata3.md) |  | [optional] 

## Example

```python
from odin_sdk.models.knowledge_base_page_item import KnowledgeBasePageItem

# TODO update the JSON string below
json = "{}"
# create an instance of KnowledgeBasePageItem from a JSON string
knowledge_base_page_item_instance = KnowledgeBasePageItem.from_json(json)
# print the JSON string representation of the object
print KnowledgeBasePageItem.to_json()

# convert the object into a dict
knowledge_base_page_item_dict = knowledge_base_page_item_instance.to_dict()
# create an instance of KnowledgeBasePageItem from a dict
knowledge_base_page_item_form_dict = knowledge_base_page_item.from_dict(knowledge_base_page_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


