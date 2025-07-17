# ExecuteActionOnTableResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **object** |  | 
**chat_id** | **object** |  | 
**message_id** | **object** |  | 
**flow_run_id** | **object** |  | 

## Example

```python
from odin_sdk.models.execute_action_on_table_response import ExecuteActionOnTableResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ExecuteActionOnTableResponse from a JSON string
execute_action_on_table_response_instance = ExecuteActionOnTableResponse.from_json(json)
# print the JSON string representation of the object
print ExecuteActionOnTableResponse.to_json()

# convert the object into a dict
execute_action_on_table_response_dict = execute_action_on_table_response_instance.to_dict()
# create an instance of ExecuteActionOnTableResponse from a dict
execute_action_on_table_response_form_dict = execute_action_on_table_response.from_dict(execute_action_on_table_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


