# RoutesToolsToolsModelsExecutionHistoryResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**runs** | [**List[WorkflowExecutionResponse]**](WorkflowExecutionResponse.md) | List of execution runs | 
**total_count** | **int** | Total number of runs available | 
**page** | **int** | Current page number | 
**page_size** | **int** | Number of runs per page | 

## Example

```python
from odin_sdk.models.routes_tools_tools_models_execution_history_response import RoutesToolsToolsModelsExecutionHistoryResponse

# TODO update the JSON string below
json = "{}"
# create an instance of RoutesToolsToolsModelsExecutionHistoryResponse from a JSON string
routes_tools_tools_models_execution_history_response_instance = RoutesToolsToolsModelsExecutionHistoryResponse.from_json(json)
# print the JSON string representation of the object
print(RoutesToolsToolsModelsExecutionHistoryResponse.to_json())

# convert the object into a dict
routes_tools_tools_models_execution_history_response_dict = routes_tools_tools_models_execution_history_response_instance.to_dict()
# create an instance of RoutesToolsToolsModelsExecutionHistoryResponse from a dict
routes_tools_tools_models_execution_history_response_from_dict = RoutesToolsToolsModelsExecutionHistoryResponse.from_dict(routes_tools_tools_models_execution_history_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


