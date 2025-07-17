# CreateViewRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **object** | Name of the view | 
**description** | [**Description6**](Description6.md) |  | [optional] 
**type** | **object** | Type of view (grid, kanban, etc) | [optional] 
**sort** | [**Sort**](Sort.md) |  | [optional] 
**filter** | [**Filter**](Filter.md) |  | [optional] 
**group** | [**Group**](Group.md) |  | [optional] 
**options** | [**Options1**](Options1.md) |  | [optional] 
**settings** | [**Settings**](Settings.md) |  | [optional] 
**column_meta** | [**ColumnMeta**](ColumnMeta.md) |  | [optional] 
**enable_share** | [**EnableShare**](EnableShare.md) |  | [optional] 

## Example

```python
from odin_sdk.models.create_view_request import CreateViewRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateViewRequest from a JSON string
create_view_request_instance = CreateViewRequest.from_json(json)
# print the JSON string representation of the object
print CreateViewRequest.to_json()

# convert the object into a dict
create_view_request_dict = create_view_request_instance.to_dict()
# create an instance of CreateViewRequest from a dict
create_view_request_form_dict = create_view_request.from_dict(create_view_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


