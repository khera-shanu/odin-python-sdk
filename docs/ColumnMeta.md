# ColumnMeta

Column metadata including width, order, visibility

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from odin_sdk.models.column_meta import ColumnMeta

# TODO update the JSON string below
json = "{}"
# create an instance of ColumnMeta from a JSON string
column_meta_instance = ColumnMeta.from_json(json)
# print the JSON string representation of the object
print ColumnMeta.to_json()

# convert the object into a dict
column_meta_dict = column_meta_instance.to_dict()
# create an instance of ColumnMeta from a dict
column_meta_form_dict = column_meta.from_dict(column_meta_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


