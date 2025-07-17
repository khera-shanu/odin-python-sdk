# UpdateViewRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | [**Name3**](Name3.md) |  | [optional] 
**description** | [**Description12**](Description12.md) |  | [optional] 
**type** | [**Type6**](Type6.md) |  | [optional] 
**sort** | [**Sort**](Sort.md) |  | [optional] 
**filter** | [**Filter**](Filter.md) |  | [optional] 
**group** | [**Group**](Group.md) |  | [optional] 
**options** | [**Options3**](Options3.md) |  | [optional] 
**settings** | [**Settings2**](Settings2.md) |  | [optional] 
**column_meta** | [**ColumnMeta**](ColumnMeta.md) |  | [optional] 
**enable_share** | [**EnableShare1**](EnableShare1.md) |  | [optional] 

## Example

```python
from odin_sdk.models.update_view_request import UpdateViewRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateViewRequest from a JSON string
update_view_request_instance = UpdateViewRequest.from_json(json)
# print the JSON string representation of the object
print UpdateViewRequest.to_json()

# convert the object into a dict
update_view_request_dict = update_view_request_instance.to_dict()
# create an instance of UpdateViewRequest from a dict
update_view_request_form_dict = update_view_request.from_dict(update_view_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


