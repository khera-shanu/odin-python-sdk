# odin_sdk.ExecutionHistoryApi

All URIs are relative to *https://127.0.0.1:8001*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_execution_history_tools_execution_history_get**](ExecutionHistoryApi.md#get_execution_history_tools_execution_history_get) | **GET** /tools/execution-history | Get Execution History
[**get_execution_run_details_tools_execution_history_run_id_get**](ExecutionHistoryApi.md#get_execution_run_details_tools_execution_history_run_id_get) | **GET** /tools/execution-history/{run_id} | Get Execution Run Details


# **get_execution_history_tools_execution_history_get**
> RoutesToolsToolsModelsExecutionHistoryResponse get_execution_history_tools_execution_history_get(project_id, tool_id=tool_id, run_kind=run_kind, execution_status=execution_status, correlation_id=correlation_id, page=page, page_size=page_size, order_by=order_by, order_desc=order_desc, x_api_key=x_api_key, x_api_secret=x_api_secret)

Get Execution History

Get execution history for workflows/tools

### Example


```python
import odin_sdk
from odin_sdk.models.routes_tools_tools_models_execution_history_response import RoutesToolsToolsModelsExecutionHistoryResponse
from odin_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://127.0.0.1:8001
# See configuration.py for a list of all supported configuration parameters.
configuration = odin_sdk.Configuration(
    host = "https://127.0.0.1:8001"
)


# Enter a context with an instance of the API client
with odin_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = odin_sdk.ExecutionHistoryApi(api_client)
    project_id = 'project_id_example' # str | 
    tool_id = 'tool_id_example' # str |  (optional)
    run_kind = 'run_kind_example' # str |  (optional)
    execution_status = 'execution_status_example' # str |  (optional)
    correlation_id = 'correlation_id_example' # str |  (optional)
    page = 1 # int |  (optional) (default to 1)
    page_size = 50 # int |  (optional) (default to 50)
    order_by = 'started_at' # str |  (optional) (default to 'started_at')
    order_desc = True # bool |  (optional) (default to True)
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Get Execution History
        api_response = api_instance.get_execution_history_tools_execution_history_get(project_id, tool_id=tool_id, run_kind=run_kind, execution_status=execution_status, correlation_id=correlation_id, page=page, page_size=page_size, order_by=order_by, order_desc=order_desc, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of ExecutionHistoryApi->get_execution_history_tools_execution_history_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExecutionHistoryApi->get_execution_history_tools_execution_history_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **tool_id** | **str**|  | [optional] 
 **run_kind** | **str**|  | [optional] 
 **execution_status** | **str**|  | [optional] 
 **correlation_id** | **str**|  | [optional] 
 **page** | **int**|  | [optional] [default to 1]
 **page_size** | **int**|  | [optional] [default to 50]
 **order_by** | **str**|  | [optional] [default to &#39;started_at&#39;]
 **order_desc** | **bool**|  | [optional] [default to True]
 **x_api_key** | **str**| Your Odin API key. | [optional] 
 **x_api_secret** | **str**| Your Odin API secret. | [optional] 

### Return type

[**RoutesToolsToolsModelsExecutionHistoryResponse**](RoutesToolsToolsModelsExecutionHistoryResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_execution_run_details_tools_execution_history_run_id_get**
> WorkflowExecutionResponse get_execution_run_details_tools_execution_history_run_id_get(run_id, x_api_key=x_api_key, x_api_secret=x_api_secret)

Get Execution Run Details

Get detailed information about a specific execution run

### Example


```python
import odin_sdk
from odin_sdk.models.workflow_execution_response import WorkflowExecutionResponse
from odin_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://127.0.0.1:8001
# See configuration.py for a list of all supported configuration parameters.
configuration = odin_sdk.Configuration(
    host = "https://127.0.0.1:8001"
)


# Enter a context with an instance of the API client
with odin_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = odin_sdk.ExecutionHistoryApi(api_client)
    run_id = 'run_id_example' # str | 
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Get Execution Run Details
        api_response = api_instance.get_execution_run_details_tools_execution_history_run_id_get(run_id, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of ExecutionHistoryApi->get_execution_run_details_tools_execution_history_run_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExecutionHistoryApi->get_execution_run_details_tools_execution_history_run_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **run_id** | **str**|  | 
 **x_api_key** | **str**| Your Odin API key. | [optional] 
 **x_api_secret** | **str**| Your Odin API secret. | [optional] 

### Return type

[**WorkflowExecutionResponse**](WorkflowExecutionResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

