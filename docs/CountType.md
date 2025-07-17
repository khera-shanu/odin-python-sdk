# CountType

Type of count for COUNT aggregations: total, true, false, null, non_null, distinct, conditional

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from odin_sdk.models.count_type import CountType

# TODO update the JSON string below
json = "{}"
# create an instance of CountType from a JSON string
count_type_instance = CountType.from_json(json)
# print the JSON string representation of the object
print CountType.to_json()

# convert the object into a dict
count_type_dict = count_type_instance.to_dict()
# create an instance of CountType from a dict
count_type_form_dict = count_type.from_dict(count_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


