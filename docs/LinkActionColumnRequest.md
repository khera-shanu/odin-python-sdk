# LinkActionColumnRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | **object** | The project ID | 
**data_type_id** | **object** | The data type ID of the table | 
**action_column_name** | **object** | The name of the column containing the action | 
**target_column_name** | **object** | The name of the column to map the action output to | 
**key_path** | **object** | The path to extract from action output | 

## Example

```python
from odin_sdk.models.link_action_column_request import LinkActionColumnRequest

# TODO update the JSON string below
json = "{}"
# create an instance of LinkActionColumnRequest from a JSON string
link_action_column_request_instance = LinkActionColumnRequest.from_json(json)
# print the JSON string representation of the object
print LinkActionColumnRequest.to_json()

# convert the object into a dict
link_action_column_request_dict = link_action_column_request_instance.to_dict()
# create an instance of LinkActionColumnRequest from a dict
link_action_column_request_form_dict = link_action_column_request.from_dict(link_action_column_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


