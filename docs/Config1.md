# Config1

Configuration for the SQL connection.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**username** | **object** | Username for the OracleSQL database. | 
**password** | **object** | Password for the OracleSQL database. | 
**host** | **object** | Host for the OracleSQL database. | 
**port** | **object** | Port for the OracleSQL database. | 
**database** | [**Database**](Database.md) |  | 
**tables** | **object** | List of tables to be used in the OracleSQL database. | 
**connectstring** | **object** | Connection string for the SQL database. | 
**always_trust_server** | [**AlwaysTrustServer**](AlwaysTrustServer.md) |  | [optional] 
**account** | **object** | Account for the SnowflakeSQL database. | 
**var_schema** | **object** | Schema for the OracleSQL database. | 
**warehouse** | **object** | Warehouse for the SnowflakeSQL database. | 
**role** | **object** | Role for the SnowflakeSQL database. | 
**service_name** | [**ServiceName**](ServiceName.md) |  | [optional] 

## Example

```python
from odin_sdk.models.config1 import Config1

# TODO update the JSON string below
json = "{}"
# create an instance of Config1 from a JSON string
config1_instance = Config1.from_json(json)
# print the JSON string representation of the object
print Config1.to_json()

# convert the object into a dict
config1_dict = config1_instance.to_dict()
# create an instance of Config1 from a dict
config1_form_dict = config1.from_dict(config1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


