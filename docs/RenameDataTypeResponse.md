# RenameDataTypeResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **object** |  | 
**data_type_id** | **object** |  | 
**new_title** | **object** |  | 

## Example

```python
from odin_sdk.models.rename_data_type_response import RenameDataTypeResponse

# TODO update the JSON string below
json = "{}"
# create an instance of RenameDataTypeResponse from a JSON string
rename_data_type_response_instance = RenameDataTypeResponse.from_json(json)
# print the JSON string representation of the object
print RenameDataTypeResponse.to_json()

# convert the object into a dict
rename_data_type_response_dict = rename_data_type_response_instance.to_dict()
# create an instance of RenameDataTypeResponse from a dict
rename_data_type_response_form_dict = rename_data_type_response.from_dict(rename_data_type_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


