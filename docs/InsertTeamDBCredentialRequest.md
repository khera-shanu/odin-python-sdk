# InsertTeamDBCredentialRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dbname** | **object** |  | 
**dbuser** | **object** |  | 
**password** | **object** |  | 
**host** | **object** |  | 
**port** | **object** |  | 
**project_url** | **object** |  | 
**project_api_key** | **object** |  | 

## Example

```python
from odin_sdk.models.insert_team_db_credential_request import InsertTeamDBCredentialRequest

# TODO update the JSON string below
json = "{}"
# create an instance of InsertTeamDBCredentialRequest from a JSON string
insert_team_db_credential_request_instance = InsertTeamDBCredentialRequest.from_json(json)
# print the JSON string representation of the object
print InsertTeamDBCredentialRequest.to_json()

# convert the object into a dict
insert_team_db_credential_request_dict = insert_team_db_credential_request_instance.to_dict()
# create an instance of InsertTeamDBCredentialRequest from a dict
insert_team_db_credential_request_form_dict = insert_team_db_credential_request.from_dict(insert_team_db_credential_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


