# AdditionalInstructions

Additional instructions to provide to the AI, provided as an array of strings.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from odin_sdk.models.additional_instructions import AdditionalInstructions

# TODO update the JSON string below
json = "{}"
# create an instance of AdditionalInstructions from a JSON string
additional_instructions_instance = AdditionalInstructions.from_json(json)
# print the JSON string representation of the object
print AdditionalInstructions.to_json()

# convert the object into a dict
additional_instructions_dict = additional_instructions_instance.to_dict()
# create an instance of AdditionalInstructions from a dict
additional_instructions_form_dict = additional_instructions.from_dict(additional_instructions_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


