# PromptDebug

Enable prompt debugging

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from odin_sdk.models.prompt_debug import PromptDebug

# TODO update the JSON string below
json = "{}"
# create an instance of PromptDebug from a JSON string
prompt_debug_instance = PromptDebug.from_json(json)
# print the JSON string representation of the object
print PromptDebug.to_json()

# convert the object into a dict
prompt_debug_dict = prompt_debug_instance.to_dict()
# create an instance of PromptDebug from a dict
prompt_debug_form_dict = prompt_debug.from_dict(prompt_debug_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


