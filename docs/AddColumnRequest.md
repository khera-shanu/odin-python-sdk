# AddColumnRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**column_name** | **object** | The name of the new column | 
**column_type** | **object** | The SQL data type for the column | 
**default_value** | **object** | Default value for the column | [optional] 
**description** | [**Description**](Description.md) |  | [optional] 
**options** | [**Options**](Options.md) |  | [optional] 

## Example

```python
from odin_sdk.models.add_column_request import AddColumnRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AddColumnRequest from a JSON string
add_column_request_instance = AddColumnRequest.from_json(json)
# print the JSON string representation of the object
print AddColumnRequest.to_json()

# convert the object into a dict
add_column_request_dict = add_column_request_instance.to_dict()
# create an instance of AddColumnRequest from a dict
add_column_request_form_dict = add_column_request.from_dict(add_column_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


