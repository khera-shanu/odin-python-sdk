# Kwargs


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from odin_sdk.models.kwargs import Kwargs

# TODO update the JSON string below
json = "{}"
# create an instance of Kwargs from a JSON string
kwargs_instance = Kwargs.from_json(json)
# print the JSON string representation of the object
print Kwargs.to_json()

# convert the object into a dict
kwargs_dict = kwargs_instance.to_dict()
# create an instance of Kwargs from a dict
kwargs_form_dict = kwargs.from_dict(kwargs_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


