# MySQLConfig


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**username** | **object** | Username for the MySQL database. | 
**password** | **object** | Password for the MySQL database. | 
**host** | **object** | Host for the MySQL database. | 
**port** | **object** | Port for the MySQL database. | 
**database** | **object** | Database name for the MySQL database. | 
**tables** | **object** | List of tables to be used in the MySQL database. | 

## Example

```python
from odin_sdk.models.my_sql_config import MySQLConfig

# TODO update the JSON string below
json = "{}"
# create an instance of MySQLConfig from a JSON string
my_sql_config_instance = MySQLConfig.from_json(json)
# print the JSON string representation of the object
print MySQLConfig.to_json()

# convert the object into a dict
my_sql_config_dict = my_sql_config_instance.to_dict()
# create an instance of MySQLConfig from a dict
my_sql_config_form_dict = my_sql_config.from_dict(my_sql_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


