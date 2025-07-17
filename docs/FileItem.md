# FileItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **object** |  | 
**key** | [**Key**](Key.md) |  | 
**path** | **object** |  | 
**size** | [**Size**](Size.md) |  | [optional] 
**type** | **object** |  | 
**created_at** | [**CreatedAt1**](CreatedAt1.md) |  | [optional] 
**updated_at** | [**UpdatedAt1**](UpdatedAt1.md) |  | [optional] 

## Example

```python
from odin_sdk.models.file_item import FileItem

# TODO update the JSON string below
json = "{}"
# create an instance of FileItem from a JSON string
file_item_instance = FileItem.from_json(json)
# print the JSON string representation of the object
print FileItem.to_json()

# convert the object into a dict
file_item_dict = file_item_instance.to_dict()
# create an instance of FileItem from a dict
file_item_form_dict = file_item.from_dict(file_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


