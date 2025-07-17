# RoutesDataTypesAddDataTypeRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data_type_id** | [**DataTypeId2**](DataTypeId2.md) |  | [optional] 
**title** | **object** | The title of the Data type. | 
**description** | **object** | A brief description of the Data type. | 
**metadata** | [**Metadata4**](Metadata4.md) |  | [optional] 

## Example

```python
from odin_sdk.models.routes_data_types_add_data_type_request import RoutesDataTypesAddDataTypeRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RoutesDataTypesAddDataTypeRequest from a JSON string
routes_data_types_add_data_type_request_instance = RoutesDataTypesAddDataTypeRequest.from_json(json)
# print the JSON string representation of the object
print RoutesDataTypesAddDataTypeRequest.to_json()

# convert the object into a dict
routes_data_types_add_data_type_request_dict = routes_data_types_add_data_type_request_instance.to_dict()
# create an instance of RoutesDataTypesAddDataTypeRequest from a dict
routes_data_types_add_data_type_request_form_dict = routes_data_types_add_data_type_request.from_dict(routes_data_types_add_data_type_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


