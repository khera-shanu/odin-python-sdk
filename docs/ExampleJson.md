# ExampleJson


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from odin_sdk.models.example_json import ExampleJson

# TODO update the JSON string below
json = "{}"
# create an instance of ExampleJson from a JSON string
example_json_instance = ExampleJson.from_json(json)
# print the JSON string representation of the object
print ExampleJson.to_json()

# convert the object into a dict
example_json_dict = example_json_instance.to_dict()
# create an instance of ExampleJson from a dict
example_json_form_dict = example_json.from_dict(example_json_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


