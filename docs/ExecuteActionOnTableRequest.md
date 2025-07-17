# ExecuteActionOnTableRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | **object** |  | 
**flow_id** | **object** |  | 
**column_name** | **object** |  | 
**action_name** | **object** |  | 
**ui_form** | **object** |  | 

## Example

```python
from odin_sdk.models.execute_action_on_table_request import ExecuteActionOnTableRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ExecuteActionOnTableRequest from a JSON string
execute_action_on_table_request_instance = ExecuteActionOnTableRequest.from_json(json)
# print the JSON string representation of the object
print ExecuteActionOnTableRequest.to_json()

# convert the object into a dict
execute_action_on_table_request_dict = execute_action_on_table_request_instance.to_dict()
# create an instance of ExecuteActionOnTableRequest from a dict
execute_action_on_table_request_form_dict = execute_action_on_table_request.from_dict(execute_action_on_table_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


