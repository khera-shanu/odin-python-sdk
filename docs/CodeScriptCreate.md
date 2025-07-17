# CodeScriptCreate

Request model for creating a new code script (draft)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **object** | Script name | 
**description** | [**Description3**](Description3.md) |  | [optional] 
**project_id** | **object** | Project ID | 
**script** | **object** | Script code | 
**runtime** | **object** | Runtime version | 
**entry_point** | **object** | Entry point function name | [optional] 
**dependencies** | **object** | List of package dependencies | [optional] 
**custom_resource_settings** | [**CustomResourceSettings**](CustomResourceSettings.md) |  | [optional] 

## Example

```python
from odin_sdk.models.code_script_create import CodeScriptCreate

# TODO update the JSON string below
json = "{}"
# create an instance of CodeScriptCreate from a JSON string
code_script_create_instance = CodeScriptCreate.from_json(json)
# print the JSON string representation of the object
print CodeScriptCreate.to_json()

# convert the object into a dict
code_script_create_dict = code_script_create_instance.to_dict()
# create an instance of CodeScriptCreate from a dict
code_script_create_form_dict = code_script_create.from_dict(code_script_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


