# ResponseGetStepResultToolsStepResultProjectIdToolIdStepIdGet


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **object** | Whether the step execution was successful | 
**message** | **object** | A message describing the result | 
**data** | [**Data**](Data.md) |  | [optional] 
**error** | [**Error2**](Error2.md) |  | [optional] 
**execution_time_ms** | [**ExecutionTimeMs1**](ExecutionTimeMs1.md) |  | [optional] 

## Example

```python
from odin_sdk.models.response_get_step_result_tools_step_result_project_id_tool_id_step_id_get import ResponseGetStepResultToolsStepResultProjectIdToolIdStepIdGet

# TODO update the JSON string below
json = "{}"
# create an instance of ResponseGetStepResultToolsStepResultProjectIdToolIdStepIdGet from a JSON string
response_get_step_result_tools_step_result_project_id_tool_id_step_id_get_instance = ResponseGetStepResultToolsStepResultProjectIdToolIdStepIdGet.from_json(json)
# print the JSON string representation of the object
print ResponseGetStepResultToolsStepResultProjectIdToolIdStepIdGet.to_json()

# convert the object into a dict
response_get_step_result_tools_step_result_project_id_tool_id_step_id_get_dict = response_get_step_result_tools_step_result_project_id_tool_id_step_id_get_instance.to_dict()
# create an instance of ResponseGetStepResultToolsStepResultProjectIdToolIdStepIdGet from a dict
response_get_step_result_tools_step_result_project_id_tool_id_step_id_get_form_dict = response_get_step_result_tools_step_result_project_id_tool_id_step_id_get.from_dict(response_get_step_result_tools_step_result_project_id_tool_id_step_id_get_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


