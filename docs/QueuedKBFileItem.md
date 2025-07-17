# QueuedKBFileItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**document_id** | [**DocumentId**](DocumentId.md) |  | [optional] 
**url** | [**Url**](Url.md) |  | [optional] 
**project_id** | **object** |  | 
**doc_type** | **object** |  | 
**status** | **object** |  | 
**upload_date** | **object** |  | 
**metadata** | [**Metadata1**](Metadata1.md) |  | [optional] 

## Example

```python
from odin_sdk.models.queued_kb_file_item import QueuedKBFileItem

# TODO update the JSON string below
json = "{}"
# create an instance of QueuedKBFileItem from a JSON string
queued_kb_file_item_instance = QueuedKBFileItem.from_json(json)
# print the JSON string representation of the object
print QueuedKBFileItem.to_json()

# convert the object into a dict
queued_kb_file_item_dict = queued_kb_file_item_instance.to_dict()
# create an instance of QueuedKBFileItem from a dict
queued_kb_file_item_form_dict = queued_kb_file_item.from_dict(queued_kb_file_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


