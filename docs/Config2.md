# Config2

The Deploy Bot configuration (authentication, bot settings, deployment type)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from odin_sdk.models.config2 import Config2

# TODO update the JSON string below
json = "{}"
# create an instance of Config2 from a JSON string
config2_instance = Config2.from_json(json)
# print the JSON string representation of the object
print Config2.to_json()

# convert the object into a dict
config2_dict = config2_instance.to_dict()
# create an instance of Config2 from a dict
config2_form_dict = config2.from_dict(config2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


