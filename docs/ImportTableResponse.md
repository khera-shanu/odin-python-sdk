# ImportTableResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **object** |  | 
**data_type_id** | **object** |  | 
**rows_imported** | **object** |  | 

## Example

```python
from odin_sdk.models.import_table_response import ImportTableResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ImportTableResponse from a JSON string
import_table_response_instance = ImportTableResponse.from_json(json)
# print the JSON string representation of the object
print ImportTableResponse.to_json()

# convert the object into a dict
import_table_response_dict = import_table_response_instance.to_dict()
# create an instance of ImportTableResponse from a dict
import_table_response_form_dict = import_table_response.from_dict(import_table_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


