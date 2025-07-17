# CreateMCPRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**service_name** | **object** | Name of the MCP service to create | 
**transport** | **object** | Transport to use for the MCP (stdio or sse) | 
**environment_variables** | [**EnvironmentVariables**](EnvironmentVariables.md) |  | [optional] 
**headers** | [**Headers**](Headers.md) |  | [optional] 
**requires_auth** | [**RequiresAuth**](RequiresAuth.md) |  | [optional] 

## Example

```python
from odin_sdk.models.create_mcp_request import CreateMCPRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateMCPRequest from a JSON string
create_mcp_request_instance = CreateMCPRequest.from_json(json)
# print the JSON string representation of the object
print CreateMCPRequest.to_json()

# convert the object into a dict
create_mcp_request_dict = create_mcp_request_instance.to_dict()
# create an instance of CreateMCPRequest from a dict
create_mcp_request_form_dict = create_mcp_request.from_dict(create_mcp_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


