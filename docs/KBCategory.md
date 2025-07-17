# KBCategory


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**category** | [**Category**](Category.md) |  | [optional] 
**keywords** | **object** |  | 

## Example

```python
from odin_sdk.models.kb_category import KBCategory

# TODO update the JSON string below
json = "{}"
# create an instance of KBCategory from a JSON string
kb_category_instance = KBCategory.from_json(json)
# print the JSON string representation of the object
print KBCategory.to_json()

# convert the object into a dict
kb_category_dict = kb_category_instance.to_dict()
# create an instance of KBCategory from a dict
kb_category_form_dict = kb_category.from_dict(kb_category_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


