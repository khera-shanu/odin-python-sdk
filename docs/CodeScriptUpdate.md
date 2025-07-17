# CodeScriptUpdate

Request model for updating a code script

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | [**Name1**](Name1.md) |  | [optional] 
**description** | [**Description4**](Description4.md) |  | [optional] 
**script** | [**Script**](Script.md) |  | [optional] 
**runtime** | [**Runtime1**](Runtime1.md) |  | [optional] 
**entry_point** | [**EntryPoint**](EntryPoint.md) |  | [optional] 
**dependencies** | [**Dependencies**](Dependencies.md) |  | [optional] 
**custom_resource_settings** | [**CustomResourceSettings1**](CustomResourceSettings1.md) |  | [optional] 

## Example

```python
from odin_sdk.models.code_script_update import CodeScriptUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of CodeScriptUpdate from a JSON string
code_script_update_instance = CodeScriptUpdate.from_json(json)
# print the JSON string representation of the object
print CodeScriptUpdate.to_json()

# convert the object into a dict
code_script_update_dict = code_script_update_instance.to_dict()
# create an instance of CodeScriptUpdate from a dict
code_script_update_form_dict = code_script_update.from_dict(code_script_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


