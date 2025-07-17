# ModelName2

Model to use for the email generation.<br>Options are: gpt-4-1106-preview, gpt-4o-mini. Note that GPT-4 based models require a subscription.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from odin_sdk.models.model_name2 import ModelName2

# TODO update the JSON string below
json = "{}"
# create an instance of ModelName2 from a JSON string
model_name2_instance = ModelName2.from_json(json)
# print the JSON string representation of the object
print ModelName2.to_json()

# convert the object into a dict
model_name2_dict = model_name2_instance.to_dict()
# create an instance of ModelName2 from a dict
model_name2_form_dict = model_name2.from_dict(model_name2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


