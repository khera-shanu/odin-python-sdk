# CodeRunnerParameter


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **object** | Parameter name | 
**type** | [**Type**](Type.md) |  | [optional] 
**description** | [**Description2**](Description2.md) |  | [optional] 
**required** | **object** | Whether the parameter is required | [optional] 
**default_value** | [**DefaultValue**](DefaultValue.md) |  | [optional] 

## Example

```python
from odin_sdk.models.code_runner_parameter import CodeRunnerParameter

# TODO update the JSON string below
json = "{}"
# create an instance of CodeRunnerParameter from a JSON string
code_runner_parameter_instance = CodeRunnerParameter.from_json(json)
# print the JSON string representation of the object
print CodeRunnerParameter.to_json()

# convert the object into a dict
code_runner_parameter_dict = code_runner_parameter_instance.to_dict()
# create an instance of CodeRunnerParameter from a dict
code_runner_parameter_form_dict = code_runner_parameter.from_dict(code_runner_parameter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


