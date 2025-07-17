# UpdateColumnMetadataRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | [**Description**](Description.md) |  | [optional] 
**type** | [**Type4**](Type4.md) |  | [optional] 
**options** | [**Options**](Options.md) |  | [optional] 
**not_null** | [**NotNull**](NotNull.md) |  | [optional] 
**unique** | [**Unique**](Unique.md) |  | [optional] 
**default_value** | [**DefaultValue2**](DefaultValue2.md) |  | [optional] 

## Example

```python
from odin_sdk.models.update_column_metadata_request import UpdateColumnMetadataRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateColumnMetadataRequest from a JSON string
update_column_metadata_request_instance = UpdateColumnMetadataRequest.from_json(json)
# print the JSON string representation of the object
print UpdateColumnMetadataRequest.to_json()

# convert the object into a dict
update_column_metadata_request_dict = update_column_metadata_request_instance.to_dict()
# create an instance of UpdateColumnMetadataRequest from a dict
update_column_metadata_request_form_dict = update_column_metadata_request.from_dict(update_column_metadata_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


