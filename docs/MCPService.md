# MCPService


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **object** |  | 
**name** | **object** |  | 
**template** | **object** |  | 
**created_timestamp** | **object** |  | 
**last_modified_timestamp** | **object** |  | 

## Example

```python
from odin_sdk.models.mcp_service import MCPService

# TODO update the JSON string below
json = "{}"
# create an instance of MCPService from a JSON string
mcp_service_instance = MCPService.from_json(json)
# print the JSON string representation of the object
print MCPService.to_json()

# convert the object into a dict
mcp_service_dict = mcp_service_instance.to_dict()
# create an instance of MCPService from a dict
mcp_service_form_dict = mcp_service.from_dict(mcp_service_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


