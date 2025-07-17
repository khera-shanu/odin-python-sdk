# CategoryOutput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**category** | [**Category**](Category.md) |  | [optional] 
**keywords** | **object** |  | 
**common_questions** | **object** |  | 

## Example

```python
from odin_sdk.models.category_output import CategoryOutput

# TODO update the JSON string below
json = "{}"
# create an instance of CategoryOutput from a JSON string
category_output_instance = CategoryOutput.from_json(json)
# print the JSON string representation of the object
print CategoryOutput.to_json()

# convert the object into a dict
category_output_dict = category_output_instance.to_dict()
# create an instance of CategoryOutput from a dict
category_output_form_dict = category_output.from_dict(category_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


