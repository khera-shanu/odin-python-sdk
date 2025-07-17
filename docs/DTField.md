# DTField


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **object** | Unique identifier for the field | 
**name** | **object** | Name of the field | 
**description** | [**Description8**](Description8.md) |  | [optional] 
**options** | [**Options2**](Options2.md) |  | [optional] 
**type** | **object** | Field type (e.g., text, number, etc.) | 
**cell_value_type** | **object** | Type of value stored in cells | 
**is_multiple_cell_value** | **object** | Whether field can contain multiple values | [optional] 
**db_field_type** | **object** | Database field type | 
**db_field_name** | **object** | Name of the field in database | 
**not_null** | **object** | Whether field is required | [optional] 
**unique** | **object** | Whether field values must be unique | [optional] 
**is_primary** | **object** | Whether field is primary key | [optional] 
**is_computed** | **object** | Whether field is computed | [optional] 
**is_lookup** | **object** | Whether field is a lookup field | [optional] 
**is_pending** | **object** | Whether field is pending creation | [optional] 
**has_error** | **object** | Whether field has errors | [optional] 
**lookup_linked_field_id** | [**LookupLinkedFieldId**](LookupLinkedFieldId.md) |  | [optional] 
**lookup_options** | [**LookupOptions**](LookupOptions.md) |  | [optional] 
**table_id** | **object** | ID of the table this field belongs to | 
**version** | **object** | Version number of the field | [optional] 
**created_time** | **object** | Creation timestamp | [optional] 
**last_modified_time** | [**LastModifiedTime**](LastModifiedTime.md) |  | [optional] 
**deleted_time** | [**DeletedTime**](DeletedTime.md) |  | [optional] 
**created_by** | **object** | User ID who created the field | 
**last_modified_by** | [**LastModifiedBy**](LastModifiedBy.md) |  | [optional] 

## Example

```python
from odin_sdk.models.dt_field import DTField

# TODO update the JSON string below
json = "{}"
# create an instance of DTField from a JSON string
dt_field_instance = DTField.from_json(json)
# print the JSON string representation of the object
print DTField.to_json()

# convert the object into a dict
dt_field_dict = dt_field_instance.to_dict()
# create an instance of DTField from a dict
dt_field_form_dict = dt_field.from_dict(dt_field_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


