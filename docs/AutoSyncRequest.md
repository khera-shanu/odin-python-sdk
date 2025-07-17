# AutoSyncRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**interval_seconds** | **object** |  | 
**project_id** | **object** |  | 
**blacklisted_docs** | [**BlacklistedDocs**](BlacklistedDocs.md) |  | [optional] 

## Example

```python
from odin_sdk.models.auto_sync_request import AutoSyncRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AutoSyncRequest from a JSON string
auto_sync_request_instance = AutoSyncRequest.from_json(json)
# print the JSON string representation of the object
print AutoSyncRequest.to_json()

# convert the object into a dict
auto_sync_request_dict = auto_sync_request_instance.to_dict()
# create an instance of AutoSyncRequest from a dict
auto_sync_request_form_dict = auto_sync_request.from_dict(auto_sync_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


