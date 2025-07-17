# FileData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**doc_type** | **object** |  | 
**url** | [**Url**](Url.md) |  | [optional] 
**metadata** | **object** |  | 
**resource_type_id** | [**ResourceTypeId**](ResourceTypeId.md) |  | [optional] 

## Example

```python
from odin_sdk.models.file_data import FileData

# TODO update the JSON string below
json = "{}"
# create an instance of FileData from a JSON string
file_data_instance = FileData.from_json(json)
# print the JSON string representation of the object
print FileData.to_json()

# convert the object into a dict
file_data_dict = file_data_instance.to_dict()
# create an instance of FileData from a dict
file_data_form_dict = file_data.from_dict(file_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


