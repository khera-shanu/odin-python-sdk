# CodeScriptResponse

Response model for code script

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **object** |  | 
**user_id** | **object** |  | 
**project_id** | **object** |  | 
**name** | **object** |  | 
**description** | [**Description1**](Description1.md) |  | 
**created_at** | **object** |  | 
**updated_at** | **object** |  | 
**script** | **object** |  | 
**runtime** | **object** |  | 
**entry_point** | **object** |  | 
**dependencies** | **object** |  | 
**custom_resource_settings** | [**CustomResourceSettings1**](CustomResourceSettings1.md) |  | 
**is_published** | **object** |  | 
**version** | [**Version**](Version.md) |  | 
**published_at** | [**PublishedAt**](PublishedAt.md) |  | 

## Example

```python
from odin_sdk.models.code_script_response import CodeScriptResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CodeScriptResponse from a JSON string
code_script_response_instance = CodeScriptResponse.from_json(json)
# print the JSON string representation of the object
print CodeScriptResponse.to_json()

# convert the object into a dict
code_script_response_dict = code_script_response_instance.to_dict()
# create an instance of CodeScriptResponse from a dict
code_script_response_form_dict = code_script_response.from_dict(code_script_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


