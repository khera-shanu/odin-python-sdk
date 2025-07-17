# StateFile

State File ensures that the filings are not processed again

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from odin_sdk.models.state_file import StateFile

# TODO update the JSON string below
json = "{}"
# create an instance of StateFile from a JSON string
state_file_instance = StateFile.from_json(json)
# print the JSON string representation of the object
print StateFile.to_json()

# convert the object into a dict
state_file_dict = state_file_instance.to_dict()
# create an instance of StateFile from a dict
state_file_form_dict = state_file.from_dict(state_file_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


