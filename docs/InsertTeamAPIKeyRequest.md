# InsertTeamAPIKeyRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key_type** | **object** |  | 
**api_key** | **object** |  | 
**azure_resource_name** | [**AzureResourceName**](AzureResourceName.md) |  | [optional] 
**azure_deployment_id** | [**AzureDeploymentId**](AzureDeploymentId.md) |  | [optional] 
**azure_openai_api_version** | [**AzureOpenaiApiVersion**](AzureOpenaiApiVersion.md) |  | [optional] 

## Example

```python
from odin_sdk.models.insert_team_api_key_request import InsertTeamAPIKeyRequest

# TODO update the JSON string below
json = "{}"
# create an instance of InsertTeamAPIKeyRequest from a JSON string
insert_team_api_key_request_instance = InsertTeamAPIKeyRequest.from_json(json)
# print the JSON string representation of the object
print InsertTeamAPIKeyRequest.to_json()

# convert the object into a dict
insert_team_api_key_request_dict = insert_team_api_key_request_instance.to_dict()
# create an instance of InsertTeamAPIKeyRequest from a dict
insert_team_api_key_request_form_dict = insert_team_api_key_request.from_dict(insert_team_api_key_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


