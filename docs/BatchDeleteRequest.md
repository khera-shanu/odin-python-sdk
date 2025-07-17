# BatchDeleteRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | **object** |  | 
**resources** | **object** |  | 

## Example

```python
from odin_sdk.models.batch_delete_request import BatchDeleteRequest

# TODO update the JSON string below
json = "{}"
# create an instance of BatchDeleteRequest from a JSON string
batch_delete_request_instance = BatchDeleteRequest.from_json(json)
# print the JSON string representation of the object
print BatchDeleteRequest.to_json()

# convert the object into a dict
batch_delete_request_dict = batch_delete_request_instance.to_dict()
# create an instance of BatchDeleteRequest from a dict
batch_delete_request_form_dict = batch_delete_request.from_dict(batch_delete_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


