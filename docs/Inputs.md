# Inputs

Tool inputs configuration

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from odin_sdk.models.inputs import Inputs

# TODO update the JSON string below
json = "{}"
# create an instance of Inputs from a JSON string
inputs_instance = Inputs.from_json(json)
# print the JSON string representation of the object
print Inputs.to_json()

# convert the object into a dict
inputs_dict = inputs_instance.to_dict()
# create an instance of Inputs from a dict
inputs_form_dict = inputs.from_dict(inputs_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


