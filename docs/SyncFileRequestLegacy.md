# SyncFileRequestLegacy


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** |  | 
**project_id** | **str** |  | 
**metadata** | **object** |  | [optional] 
**resource_type_id** | **str** |  | [optional] 
**is_quick_upload** | **bool** |  | [optional] 
**path** | **str** |  | [optional] 

## Example

```python
from odin_sdk.models.sync_file_request_legacy import SyncFileRequestLegacy

# TODO update the JSON string below
json = "{}"
# create an instance of SyncFileRequestLegacy from a JSON string
sync_file_request_legacy_instance = SyncFileRequestLegacy.from_json(json)
# print the JSON string representation of the object
print(SyncFileRequestLegacy.to_json())

# convert the object into a dict
sync_file_request_legacy_dict = sync_file_request_legacy_instance.to_dict()
# create an instance of SyncFileRequestLegacy from a dict
sync_file_request_legacy_from_dict = SyncFileRequestLegacy.from_dict(sync_file_request_legacy_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


