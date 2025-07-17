# Steps

Tool steps configuration

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from odin_sdk.models.steps import Steps

# TODO update the JSON string below
json = "{}"
# create an instance of Steps from a JSON string
steps_instance = Steps.from_json(json)
# print the JSON string representation of the object
print Steps.to_json()

# convert the object into a dict
steps_dict = steps_instance.to_dict()
# create an instance of Steps from a dict
steps_form_dict = steps.from_dict(steps_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


