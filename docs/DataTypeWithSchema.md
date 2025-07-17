# DataTypeWithSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **object** |  | 
**project_id** | **object** |  | 
**table_id** | **object** |  | 
**title** | **object** |  | 
**description** | **object** |  | 
**metadata** | **object** |  | 
**table_name** | **object** |  | 
**var_schema** | **object** |  | 

## Example

```python
from odin_sdk.models.data_type_with_schema import DataTypeWithSchema

# TODO update the JSON string below
json = "{}"
# create an instance of DataTypeWithSchema from a JSON string
data_type_with_schema_instance = DataTypeWithSchema.from_json(json)
# print the JSON string representation of the object
print DataTypeWithSchema.to_json()

# convert the object into a dict
data_type_with_schema_dict = data_type_with_schema_instance.to_dict()
# create an instance of DataTypeWithSchema from a dict
data_type_with_schema_form_dict = data_type_with_schema.from_dict(data_type_with_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


