# Filters2

Filters to apply to the query. Available default fields for filters: upload_date, status, doc_type, added_by.             Additional fields defined by user can also be added to filters

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from odin_sdk.models.filters2 import Filters2

# TODO update the JSON string below
json = "{}"
# create an instance of Filters2 from a JSON string
filters2_instance = Filters2.from_json(json)
# print the JSON string representation of the object
print Filters2.to_json()

# convert the object into a dict
filters2_dict = filters2_instance.to_dict()
# create an instance of Filters2 from a dict
filters2_form_dict = filters2.from_dict(filters2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


