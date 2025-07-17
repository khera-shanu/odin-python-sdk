# ColumnNames

Optional list of column names to compute. If not provided, all LLM-configured columns will be computed

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from odin_sdk.models.column_names import ColumnNames

# TODO update the JSON string below
json = "{}"
# create an instance of ColumnNames from a JSON string
column_names_instance = ColumnNames.from_json(json)
# print the JSON string representation of the object
print ColumnNames.to_json()

# convert the object into a dict
column_names_dict = column_names_instance.to_dict()
# create an instance of ColumnNames from a dict
column_names_form_dict = column_names.from_dict(column_names_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


