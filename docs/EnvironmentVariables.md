# EnvironmentVariables

Additional environment variables for the MCP

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from odin_sdk.models.environment_variables import EnvironmentVariables

# TODO update the JSON string below
json = "{}"
# create an instance of EnvironmentVariables from a JSON string
environment_variables_instance = EnvironmentVariables.from_json(json)
# print the JSON string representation of the object
print EnvironmentVariables.to_json()

# convert the object into a dict
environment_variables_dict = environment_variables_instance.to_dict()
# create an instance of EnvironmentVariables from a dict
environment_variables_form_dict = environment_variables.from_dict(environment_variables_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


