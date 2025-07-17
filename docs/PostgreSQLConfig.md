# PostgreSQLConfig


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**username** | **object** | Username for the PostgreSQL database. | 
**password** | **object** | Password for the PostgreSQL database. | 
**host** | **object** | Host for the PostgreSQL database. | 
**port** | **object** | Port for the PostgreSQL database. | 
**database** | **object** | Database name for the PostgreSQL database. | 
**tables** | **object** | List of tables to be used in the PostgreSQL database. | 

## Example

```python
from odin_sdk.models.postgre_sql_config import PostgreSQLConfig

# TODO update the JSON string below
json = "{}"
# create an instance of PostgreSQLConfig from a JSON string
postgre_sql_config_instance = PostgreSQLConfig.from_json(json)
# print the JSON string representation of the object
print PostgreSQLConfig.to_json()

# convert the object into a dict
postgre_sql_config_dict = postgre_sql_config_instance.to_dict()
# create an instance of PostgreSQLConfig from a dict
postgre_sql_config_form_dict = postgre_sql_config.from_dict(postgre_sql_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


