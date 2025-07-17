# SyncFileRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **object** |  | 
**project_id** | **object** |  | 
**metadata** | [**Metadata1**](Metadata1.md) |  | [optional] 
**resource_type_id** | [**ResourceTypeId**](ResourceTypeId.md) |  | [optional] 
**is_quick_upload** | [**IsQuickUpload**](IsQuickUpload.md) |  | [optional] 
**path** | [**Path**](Path.md) |  | [optional] 

## Example

```python
from odin_sdk.models.sync_file_request import SyncFileRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SyncFileRequest from a JSON string
sync_file_request_instance = SyncFileRequest.from_json(json)
# print the JSON string representation of the object
print SyncFileRequest.to_json()

# convert the object into a dict
sync_file_request_dict = sync_file_request_instance.to_dict()
# create an instance of SyncFileRequest from a dict
sync_file_request_form_dict = sync_file_request.from_dict(sync_file_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


