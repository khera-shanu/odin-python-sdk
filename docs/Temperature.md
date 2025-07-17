# Temperature

Creativity of the AI, float from 0 to 1, where 0 is the least creative and 1 is the most creative.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from odin_sdk.models.temperature import Temperature

# TODO update the JSON string below
json = "{}"
# create an instance of Temperature from a JSON string
temperature_instance = Temperature.from_json(json)
# print the JSON string representation of the object
print Temperature.to_json()

# convert the object into a dict
temperature_dict = temperature_instance.to_dict()
# create an instance of Temperature from a dict
temperature_form_dict = temperature.from_dict(temperature_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


