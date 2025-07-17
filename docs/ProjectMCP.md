# ProjectMCP


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **object** |  | 
**project_id** | **object** |  | 
**mcp_ref_id** | **object** |  | 
**service_name** | **object** |  | 
**service_configuration** | **object** |  | 
**platform** | **object** |  | 
**enabled** | **object** |  | 
**created_timestamp** | **object** |  | 
**last_modified_timestamp** | **object** |  | 

## Example

```python
from odin_sdk.models.project_mcp import ProjectMCP

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectMCP from a JSON string
project_mcp_instance = ProjectMCP.from_json(json)
# print the JSON string representation of the object
print ProjectMCP.to_json()

# convert the object into a dict
project_mcp_dict = project_mcp_instance.to_dict()
# create an instance of ProjectMCP from a dict
project_mcp_form_dict = project_mcp.from_dict(project_mcp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


