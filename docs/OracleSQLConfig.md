# OracleSQLConfig


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**username** | **object** | Username for the OracleSQL database. | 
**password** | **object** | Password for the OracleSQL database. | 
**host** | **object** | Host for the OracleSQL database. | 
**port** | **object** | Port for the OracleSQL database. | 
**database** | [**Database**](Database.md) |  | [optional] 
**service_name** | [**ServiceName**](ServiceName.md) |  | [optional] 
**tables** | **object** | List of tables to be used in the OracleSQL database. | 
**var_schema** | **object** | Schema for the OracleSQL database. | 

## Example

```python
from odin_sdk.models.oracle_sql_config import OracleSQLConfig

# TODO update the JSON string below
json = "{}"
# create an instance of OracleSQLConfig from a JSON string
oracle_sql_config_instance = OracleSQLConfig.from_json(json)
# print the JSON string representation of the object
print OracleSQLConfig.to_json()

# convert the object into a dict
oracle_sql_config_dict = oracle_sql_config_instance.to_dict()
# create an instance of OracleSQLConfig from a dict
oracle_sql_config_form_dict = oracle_sql_config.from_dict(oracle_sql_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


