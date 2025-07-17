# MSSQLConfig


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**username** | **object** | Username for the MS-SQL database. | 
**password** | **object** | Password for the MS-SQL database. | 
**host** | **object** | Host for the MS-SQL database. | 
**port** | **object** | Port for the MS-SQL database. | 
**database** | **object** | Database name for the MS-SQL database. | 
**tables** | **object** | List of tables to be used in the MS-SQL database. | 
**always_trust_server** | [**AlwaysTrustServer**](AlwaysTrustServer.md) |  | [optional] 

## Example

```python
from odin_sdk.models.mssql_config import MSSQLConfig

# TODO update the JSON string below
json = "{}"
# create an instance of MSSQLConfig from a JSON string
mssql_config_instance = MSSQLConfig.from_json(json)
# print the JSON string representation of the object
print MSSQLConfig.to_json()

# convert the object into a dict
mssql_config_dict = mssql_config_instance.to_dict()
# create an instance of MSSQLConfig from a dict
mssql_config_form_dict = mssql_config.from_dict(mssql_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


