# SnowflakeSQLConfig


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account** | **object** | Account for the SnowflakeSQL database. | 
**username** | **object** | Username for the SnowflakeSQL database. | 
**password** | **object** | Password for the SnowflakeSQL database. | 
**database** | **object** | Database for the SnowflakeSQL database. | 
**var_schema** | **object** | Schema for the SnowflakeSQL database. | 
**warehouse** | **object** | Warehouse for the SnowflakeSQL database. | 
**role** | **object** | Role for the SnowflakeSQL database. | 

## Example

```python
from odin_sdk.models.snowflake_sql_config import SnowflakeSQLConfig

# TODO update the JSON string below
json = "{}"
# create an instance of SnowflakeSQLConfig from a JSON string
snowflake_sql_config_instance = SnowflakeSQLConfig.from_json(json)
# print the JSON string representation of the object
print SnowflakeSQLConfig.to_json()

# convert the object into a dict
snowflake_sql_config_dict = snowflake_sql_config_instance.to_dict()
# create an instance of SnowflakeSQLConfig from a dict
snowflake_sql_config_form_dict = snowflake_sql_config.from_dict(snowflake_sql_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


