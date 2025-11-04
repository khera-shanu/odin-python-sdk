# odin_sdk.CustomToolsApi

All URIs are relative to *https://127.0.0.1:8001*

Method | HTTP request | Description
------------- | ------------- | -------------
[**clone_public_tool_tools_custom_clone_post**](CustomToolsApi.md#clone_public_tool_tools_custom_clone_post) | **POST** /tools/custom/clone | Clone Public Tool
[**create_custom_tool_tools_custom_post**](CustomToolsApi.md#create_custom_tool_tools_custom_post) | **POST** /tools/custom | Create Custom Tool
[**delete_custom_tool_tools_custom_tool_id_delete**](CustomToolsApi.md#delete_custom_tool_tools_custom_tool_id_delete) | **DELETE** /tools/custom/{tool_id} | Delete Custom Tool
[**execute_workflow_stream_tools_execute_workflow_stream_get**](CustomToolsApi.md#execute_workflow_stream_tools_execute_workflow_stream_get) | **GET** /tools/execute-workflow-stream | Execute Workflow Stream
[**execute_workflow_tools_execute_workflow_post**](CustomToolsApi.md#execute_workflow_tools_execute_workflow_post) | **POST** /tools/execute-workflow | Execute Workflow
[**execute_workflow_with_file_upload_tools_execute_workflow_file_upload_post**](CustomToolsApi.md#execute_workflow_with_file_upload_tools_execute_workflow_file_upload_post) | **POST** /tools/execute-workflow-file-upload | Execute Workflow With File Upload
[**export_custom_tool_tools_custom_tool_id_export_post**](CustomToolsApi.md#export_custom_tool_tools_custom_tool_id_export_post) | **POST** /tools/custom/{tool_id}/export | Export Custom Tool
[**get_available_toolkit_tools_tools_available_toolkit_tools_get**](CustomToolsApi.md#get_available_toolkit_tools_tools_available_toolkit_tools_get) | **GET** /tools/available-toolkit-tools | Get Available Toolkit Tools
[**get_custom_tool_tools_custom_tool_id_get**](CustomToolsApi.md#get_custom_tool_tools_custom_tool_id_get) | **GET** /tools/custom/{tool_id} | Get Custom Tool
[**get_custom_tools_tools_custom_get**](CustomToolsApi.md#get_custom_tools_tools_custom_get) | **GET** /tools/custom | Get Custom Tools
[**get_public_custom_tools_tools_custom_public_get**](CustomToolsApi.md#get_public_custom_tools_tools_custom_public_get) | **GET** /tools/custom/public | Get Public Custom Tools
[**get_tool_schedule_status_tools_custom_tool_id_schedule_status_get**](CustomToolsApi.md#get_tool_schedule_status_tools_custom_tool_id_schedule_status_get) | **GET** /tools/custom/{tool_id}/schedule-status | Get Tool Schedule Status
[**get_tool_version_tools_custom_tool_id_version_version_get**](CustomToolsApi.md#get_tool_version_tools_custom_tool_id_version_version_get) | **GET** /tools/custom/{tool_id}/version/{version} | Get Tool Version
[**get_tool_versions_tools_custom_tool_id_versions_get**](CustomToolsApi.md#get_tool_versions_tools_custom_tool_id_versions_get) | **GET** /tools/custom/{tool_id}/versions | Get Tool Versions
[**get_toolkit_oauth_login_url_tools_oauth_login_url_get**](CustomToolsApi.md#get_toolkit_oauth_login_url_tools_oauth_login_url_get) | **GET** /tools/oauth/login-url | Get Toolkit Oauth Login Url
[**get_toolkit_oauth_status_tools_oauth_status_get**](CustomToolsApi.md#get_toolkit_oauth_status_tools_oauth_status_get) | **GET** /tools/oauth/status | Get Toolkit Oauth Status
[**get_tools_schedule_status_batch_tools_custom_schedule_status_batch_post**](CustomToolsApi.md#get_tools_schedule_status_batch_tools_custom_schedule_status_batch_post) | **POST** /tools/custom/schedule-status/batch | Get Tools Schedule Status Batch
[**import_custom_tool_tools_custom_import_post**](CustomToolsApi.md#import_custom_tool_tools_custom_import_post) | **POST** /tools/custom/import | Import Custom Tool
[**pause_tool_schedule_tools_custom_tool_id_pause_schedule_post**](CustomToolsApi.md#pause_tool_schedule_tools_custom_tool_id_pause_schedule_post) | **POST** /tools/custom/{tool_id}/pause-schedule | Pause Tool Schedule
[**publish_custom_tool_tools_custom_tool_id_publish_post**](CustomToolsApi.md#publish_custom_tool_tools_custom_tool_id_publish_post) | **POST** /tools/custom/{tool_id}/publish | Publish Custom Tool
[**resume_tool_schedule_tools_custom_tool_id_resume_schedule_post**](CustomToolsApi.md#resume_tool_schedule_tools_custom_tool_id_resume_schedule_post) | **POST** /tools/custom/{tool_id}/resume-schedule | Resume Tool Schedule
[**revert_draft_to_version_tools_custom_tool_id_revert_to_version_post**](CustomToolsApi.md#revert_draft_to_version_tools_custom_tool_id_revert_to_version_post) | **POST** /tools/custom/{tool_id}/revert-to-version | Revert Draft To Version
[**update_custom_tool_tools_custom_tool_id_put**](CustomToolsApi.md#update_custom_tool_tools_custom_tool_id_put) | **PUT** /tools/custom/{tool_id} | Update Custom Tool


# **clone_public_tool_tools_custom_clone_post**
> CustomToolResponse clone_public_tool_tools_custom_clone_post(clone_public_tool_request, x_api_key=x_api_key, x_api_secret=x_api_secret)

Clone Public Tool

Clone a public tool to a project and automatically publish it

### Example


```python
import odin_sdk
from odin_sdk.models.clone_public_tool_request import ClonePublicToolRequest
from odin_sdk.models.custom_tool_response import CustomToolResponse
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
    api_instance = odin_sdk.CustomToolsApi(api_client)
    clone_public_tool_request = odin_sdk.ClonePublicToolRequest() # ClonePublicToolRequest | 
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Clone Public Tool
        api_response = api_instance.clone_public_tool_tools_custom_clone_post(clone_public_tool_request, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of CustomToolsApi->clone_public_tool_tools_custom_clone_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomToolsApi->clone_public_tool_tools_custom_clone_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **clone_public_tool_request** | [**ClonePublicToolRequest**](ClonePublicToolRequest.md)|  | 
 **x_api_key** | **str**| Your Odin API key. | [optional] 
 **x_api_secret** | **str**| Your Odin API secret. | [optional] 

### Return type

[**CustomToolResponse**](CustomToolResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_custom_tool_tools_custom_post**
> CustomToolResponse create_custom_tool_tools_custom_post(create_custom_tool_request, x_api_key=x_api_key, x_api_secret=x_api_secret)

Create Custom Tool

Create a new custom tool

### Example


```python
import odin_sdk
from odin_sdk.models.create_custom_tool_request import CreateCustomToolRequest
from odin_sdk.models.custom_tool_response import CustomToolResponse
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
    api_instance = odin_sdk.CustomToolsApi(api_client)
    create_custom_tool_request = odin_sdk.CreateCustomToolRequest() # CreateCustomToolRequest | 
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Create Custom Tool
        api_response = api_instance.create_custom_tool_tools_custom_post(create_custom_tool_request, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of CustomToolsApi->create_custom_tool_tools_custom_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomToolsApi->create_custom_tool_tools_custom_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_custom_tool_request** | [**CreateCustomToolRequest**](CreateCustomToolRequest.md)|  | 
 **x_api_key** | **str**| Your Odin API key. | [optional] 
 **x_api_secret** | **str**| Your Odin API secret. | [optional] 

### Return type

[**CustomToolResponse**](CustomToolResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_custom_tool_tools_custom_tool_id_delete**
> object delete_custom_tool_tools_custom_tool_id_delete(tool_id, x_api_key=x_api_key, x_api_secret=x_api_secret)

Delete Custom Tool

Delete a custom tool

### Example


```python
import odin_sdk
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
    api_instance = odin_sdk.CustomToolsApi(api_client)
    tool_id = 'tool_id_example' # str | 
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Delete Custom Tool
        api_response = api_instance.delete_custom_tool_tools_custom_tool_id_delete(tool_id, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of CustomToolsApi->delete_custom_tool_tools_custom_tool_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomToolsApi->delete_custom_tool_tools_custom_tool_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tool_id** | **str**|  | 
 **x_api_key** | **str**| Your Odin API key. | [optional] 
 **x_api_secret** | **str**| Your Odin API secret. | [optional] 

### Return type

**object**

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

# **execute_workflow_stream_tools_execute_workflow_stream_get**
> object execute_workflow_stream_tools_execute_workflow_stream_get(project_id, tool_id, tool_config=tool_config, inputs=inputs, execution_mode=execution_mode, chat_id=chat_id, message_id=message_id)

Execute Workflow Stream

Execute custom tool workflow with real-time SSE streaming

### Example


```python
import odin_sdk
from odin_sdk.models.execution_mode import ExecutionMode
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
    api_instance = odin_sdk.CustomToolsApi(api_client)
    project_id = 'project_id_example' # str | Project ID
    tool_id = 'tool_id_example' # str | Tool ID
    tool_config = 'tool_config_example' # str | Optional tool configuration JSON (fetched from DB if not provided) (optional)
    inputs = 'inputs_example' # str | Input parameters JSON (optional)
    execution_mode = odin_sdk.ExecutionMode() # ExecutionMode | Execution mode: 'workflow' or 'debug' (optional)
    chat_id = 'chat_id_example' # str | Optional chat ID for communication tools (optional)
    message_id = 'message_id_example' # str | Optional message ID for communication tools (optional)

    try:
        # Execute Workflow Stream
        api_response = api_instance.execute_workflow_stream_tools_execute_workflow_stream_get(project_id, tool_id, tool_config=tool_config, inputs=inputs, execution_mode=execution_mode, chat_id=chat_id, message_id=message_id)
        print("The response of CustomToolsApi->execute_workflow_stream_tools_execute_workflow_stream_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomToolsApi->execute_workflow_stream_tools_execute_workflow_stream_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project ID | 
 **tool_id** | **str**| Tool ID | 
 **tool_config** | **str**| Optional tool configuration JSON (fetched from DB if not provided) | [optional] 
 **inputs** | **str**| Input parameters JSON | [optional] 
 **execution_mode** | [**ExecutionMode**](.md)| Execution mode: &#39;workflow&#39; or &#39;debug&#39; | [optional] 
 **chat_id** | **str**| Optional chat ID for communication tools | [optional] 
 **message_id** | **str**| Optional message ID for communication tools | [optional] 

### Return type

**object**

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

# **execute_workflow_tools_execute_workflow_post**
> WorkflowExecutionResult execute_workflow_tools_execute_workflow_post(workflow_execution_request, x_api_key=x_api_key, x_api_secret=x_api_secret)

Execute Workflow

Execute custom tool workflow with parallel DAG execution

### Example


```python
import odin_sdk
from odin_sdk.models.workflow_execution_request import WorkflowExecutionRequest
from odin_sdk.models.workflow_execution_result import WorkflowExecutionResult
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
    api_instance = odin_sdk.CustomToolsApi(api_client)
    workflow_execution_request = odin_sdk.WorkflowExecutionRequest() # WorkflowExecutionRequest | 
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Execute Workflow
        api_response = api_instance.execute_workflow_tools_execute_workflow_post(workflow_execution_request, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of CustomToolsApi->execute_workflow_tools_execute_workflow_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomToolsApi->execute_workflow_tools_execute_workflow_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workflow_execution_request** | [**WorkflowExecutionRequest**](WorkflowExecutionRequest.md)|  | 
 **x_api_key** | **str**| Your Odin API key. | [optional] 
 **x_api_secret** | **str**| Your Odin API secret. | [optional] 

### Return type

[**WorkflowExecutionResult**](WorkflowExecutionResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **execute_workflow_with_file_upload_tools_execute_workflow_file_upload_post**
> WorkflowExecutionResult execute_workflow_with_file_upload_tools_execute_workflow_file_upload_post(file, project_id, tool_id, x_api_key=x_api_key, x_api_secret=x_api_secret, tool_config=tool_config, csv_delimiter=csv_delimiter, push_ref=push_ref)

Execute Workflow With File Upload

Directly upload a file, inject filename/filecontent inputs, and execute a workflow (bypasses queue).

### Example


```python
import odin_sdk
from odin_sdk.models.workflow_execution_result import WorkflowExecutionResult
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
    api_instance = odin_sdk.CustomToolsApi(api_client)
    file = None # bytearray | 
    project_id = 'project_id_example' # str | 
    tool_id = 'tool_id_example' # str | 
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)
    tool_config = 'tool_config_example' # str |  (optional)
    csv_delimiter = 'csv_delimiter_example' # str |  (optional)
    push_ref = 'push_ref_example' # str |  (optional)

    try:
        # Execute Workflow With File Upload
        api_response = api_instance.execute_workflow_with_file_upload_tools_execute_workflow_file_upload_post(file, project_id, tool_id, x_api_key=x_api_key, x_api_secret=x_api_secret, tool_config=tool_config, csv_delimiter=csv_delimiter, push_ref=push_ref)
        print("The response of CustomToolsApi->execute_workflow_with_file_upload_tools_execute_workflow_file_upload_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomToolsApi->execute_workflow_with_file_upload_tools_execute_workflow_file_upload_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file** | **bytearray**|  | 
 **project_id** | **str**|  | 
 **tool_id** | **str**|  | 
 **x_api_key** | **str**| Your Odin API key. | [optional] 
 **x_api_secret** | **str**| Your Odin API secret. | [optional] 
 **tool_config** | **str**|  | [optional] 
 **csv_delimiter** | **str**|  | [optional] 
 **push_ref** | **str**|  | [optional] 

### Return type

[**WorkflowExecutionResult**](WorkflowExecutionResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **export_custom_tool_tools_custom_tool_id_export_post**
> ExportToolResponse export_custom_tool_tools_custom_tool_id_export_post(tool_id, export_tool_request, x_api_key=x_api_key, x_api_secret=x_api_secret)

Export Custom Tool

Export a custom tool as JSON

### Example


```python
import odin_sdk
from odin_sdk.models.export_tool_request import ExportToolRequest
from odin_sdk.models.export_tool_response import ExportToolResponse
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
    api_instance = odin_sdk.CustomToolsApi(api_client)
    tool_id = 'tool_id_example' # str | 
    export_tool_request = odin_sdk.ExportToolRequest() # ExportToolRequest | 
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Export Custom Tool
        api_response = api_instance.export_custom_tool_tools_custom_tool_id_export_post(tool_id, export_tool_request, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of CustomToolsApi->export_custom_tool_tools_custom_tool_id_export_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomToolsApi->export_custom_tool_tools_custom_tool_id_export_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tool_id** | **str**|  | 
 **export_tool_request** | [**ExportToolRequest**](ExportToolRequest.md)|  | 
 **x_api_key** | **str**| Your Odin API key. | [optional] 
 **x_api_secret** | **str**| Your Odin API secret. | [optional] 

### Return type

[**ExportToolResponse**](ExportToolResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_available_toolkit_tools_tools_available_toolkit_tools_get**
> object get_available_toolkit_tools_tools_available_toolkit_tools_get(project_id, x_api_key=x_api_key, x_api_secret=x_api_secret)

Get Available Toolkit Tools

Get all available toolkit tools with schema introspection and auth metadata

### Example


```python
import odin_sdk
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
    api_instance = odin_sdk.CustomToolsApi(api_client)
    project_id = 'project_id_example' # str | Project ID
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Get Available Toolkit Tools
        api_response = api_instance.get_available_toolkit_tools_tools_available_toolkit_tools_get(project_id, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of CustomToolsApi->get_available_toolkit_tools_tools_available_toolkit_tools_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomToolsApi->get_available_toolkit_tools_tools_available_toolkit_tools_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project ID | 
 **x_api_key** | **str**| Your Odin API key. | [optional] 
 **x_api_secret** | **str**| Your Odin API secret. | [optional] 

### Return type

**object**

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

# **get_custom_tool_tools_custom_tool_id_get**
> CustomToolResponse get_custom_tool_tools_custom_tool_id_get(tool_id, x_api_key=x_api_key, x_api_secret=x_api_secret)

Get Custom Tool

Get a specific custom tool by ID

### Example


```python
import odin_sdk
from odin_sdk.models.custom_tool_response import CustomToolResponse
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
    api_instance = odin_sdk.CustomToolsApi(api_client)
    tool_id = 'tool_id_example' # str | 
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Get Custom Tool
        api_response = api_instance.get_custom_tool_tools_custom_tool_id_get(tool_id, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of CustomToolsApi->get_custom_tool_tools_custom_tool_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomToolsApi->get_custom_tool_tools_custom_tool_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tool_id** | **str**|  | 
 **x_api_key** | **str**| Your Odin API key. | [optional] 
 **x_api_secret** | **str**| Your Odin API secret. | [optional] 

### Return type

[**CustomToolResponse**](CustomToolResponse.md)

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

# **get_custom_tools_tools_custom_get**
> CustomToolListResponse get_custom_tools_tools_custom_get(project_id, limit=limit, offset=offset, x_api_key=x_api_key, x_api_secret=x_api_secret)

Get Custom Tools

Get all custom tools for a project

### Example


```python
import odin_sdk
from odin_sdk.models.custom_tool_list_response import CustomToolListResponse
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
    api_instance = odin_sdk.CustomToolsApi(api_client)
    project_id = 'project_id_example' # str | 
    limit = 50 # int |  (optional) (default to 50)
    offset = 0 # int |  (optional) (default to 0)
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Get Custom Tools
        api_response = api_instance.get_custom_tools_tools_custom_get(project_id, limit=limit, offset=offset, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of CustomToolsApi->get_custom_tools_tools_custom_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomToolsApi->get_custom_tools_tools_custom_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **limit** | **int**|  | [optional] [default to 50]
 **offset** | **int**|  | [optional] [default to 0]
 **x_api_key** | **str**| Your Odin API key. | [optional] 
 **x_api_secret** | **str**| Your Odin API secret. | [optional] 

### Return type

[**CustomToolListResponse**](CustomToolListResponse.md)

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

# **get_public_custom_tools_tools_custom_public_get**
> CustomToolListResponse get_public_custom_tools_tools_custom_public_get(limit=limit, offset=offset, x_api_key=x_api_key, x_api_secret=x_api_secret)

Get Public Custom Tools

Get all public custom tools from any user

### Example


```python
import odin_sdk
from odin_sdk.models.custom_tool_list_response import CustomToolListResponse
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
    api_instance = odin_sdk.CustomToolsApi(api_client)
    limit = 50 # int |  (optional) (default to 50)
    offset = 0 # int |  (optional) (default to 0)
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Get Public Custom Tools
        api_response = api_instance.get_public_custom_tools_tools_custom_public_get(limit=limit, offset=offset, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of CustomToolsApi->get_public_custom_tools_tools_custom_public_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomToolsApi->get_public_custom_tools_tools_custom_public_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**|  | [optional] [default to 50]
 **offset** | **int**|  | [optional] [default to 0]
 **x_api_key** | **str**| Your Odin API key. | [optional] 
 **x_api_secret** | **str**| Your Odin API secret. | [optional] 

### Return type

[**CustomToolListResponse**](CustomToolListResponse.md)

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

# **get_tool_schedule_status_tools_custom_tool_id_schedule_status_get**
> object get_tool_schedule_status_tools_custom_tool_id_schedule_status_get(tool_id, x_api_key=x_api_key, x_api_secret=x_api_secret)

Get Tool Schedule Status

Get schedule status for a custom tool/workflow

### Example


```python
import odin_sdk
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
    api_instance = odin_sdk.CustomToolsApi(api_client)
    tool_id = 'tool_id_example' # str | 
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Get Tool Schedule Status
        api_response = api_instance.get_tool_schedule_status_tools_custom_tool_id_schedule_status_get(tool_id, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of CustomToolsApi->get_tool_schedule_status_tools_custom_tool_id_schedule_status_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomToolsApi->get_tool_schedule_status_tools_custom_tool_id_schedule_status_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tool_id** | **str**|  | 
 **x_api_key** | **str**| Your Odin API key. | [optional] 
 **x_api_secret** | **str**| Your Odin API secret. | [optional] 

### Return type

**object**

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

# **get_tool_version_tools_custom_tool_id_version_version_get**
> CustomToolVersionResponse get_tool_version_tools_custom_tool_id_version_version_get(tool_id, version, x_api_key=x_api_key, x_api_secret=x_api_secret)

Get Tool Version

Get a specific version of a tool

### Example


```python
import odin_sdk
from odin_sdk.models.custom_tool_version_response import CustomToolVersionResponse
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
    api_instance = odin_sdk.CustomToolsApi(api_client)
    tool_id = 'tool_id_example' # str | 
    version = 'version_example' # str | 
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Get Tool Version
        api_response = api_instance.get_tool_version_tools_custom_tool_id_version_version_get(tool_id, version, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of CustomToolsApi->get_tool_version_tools_custom_tool_id_version_version_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomToolsApi->get_tool_version_tools_custom_tool_id_version_version_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tool_id** | **str**|  | 
 **version** | **str**|  | 
 **x_api_key** | **str**| Your Odin API key. | [optional] 
 **x_api_secret** | **str**| Your Odin API secret. | [optional] 

### Return type

[**CustomToolVersionResponse**](CustomToolVersionResponse.md)

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

# **get_tool_versions_tools_custom_tool_id_versions_get**
> CustomToolVersionListResponse get_tool_versions_tools_custom_tool_id_versions_get(tool_id, limit=limit, offset=offset, x_api_key=x_api_key, x_api_secret=x_api_secret)

Get Tool Versions

Get version history for a tool

### Example


```python
import odin_sdk
from odin_sdk.models.custom_tool_version_list_response import CustomToolVersionListResponse
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
    api_instance = odin_sdk.CustomToolsApi(api_client)
    tool_id = 'tool_id_example' # str | 
    limit = 20 # int |  (optional) (default to 20)
    offset = 0 # int |  (optional) (default to 0)
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Get Tool Versions
        api_response = api_instance.get_tool_versions_tools_custom_tool_id_versions_get(tool_id, limit=limit, offset=offset, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of CustomToolsApi->get_tool_versions_tools_custom_tool_id_versions_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomToolsApi->get_tool_versions_tools_custom_tool_id_versions_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tool_id** | **str**|  | 
 **limit** | **int**|  | [optional] [default to 20]
 **offset** | **int**|  | [optional] [default to 0]
 **x_api_key** | **str**| Your Odin API key. | [optional] 
 **x_api_secret** | **str**| Your Odin API secret. | [optional] 

### Return type

[**CustomToolVersionListResponse**](CustomToolVersionListResponse.md)

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

# **get_toolkit_oauth_login_url_tools_oauth_login_url_get**
> object get_toolkit_oauth_login_url_tools_oauth_login_url_get(project_id, toolkit_name, final_redirect=final_redirect, x_api_key=x_api_key, x_api_secret=x_api_secret)

Get Toolkit Oauth Login Url

Get OAuth login URL for a toolkit

### Example


```python
import odin_sdk
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
    api_instance = odin_sdk.CustomToolsApi(api_client)
    project_id = 'project_id_example' # str | Project ID
    toolkit_name = 'toolkit_name_example' # str | Toolkit name
    final_redirect = 'final_redirect_example' # str | URL to redirect to after OAuth completion (optional)
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Get Toolkit Oauth Login Url
        api_response = api_instance.get_toolkit_oauth_login_url_tools_oauth_login_url_get(project_id, toolkit_name, final_redirect=final_redirect, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of CustomToolsApi->get_toolkit_oauth_login_url_tools_oauth_login_url_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomToolsApi->get_toolkit_oauth_login_url_tools_oauth_login_url_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project ID | 
 **toolkit_name** | **str**| Toolkit name | 
 **final_redirect** | **str**| URL to redirect to after OAuth completion | [optional] 
 **x_api_key** | **str**| Your Odin API key. | [optional] 
 **x_api_secret** | **str**| Your Odin API secret. | [optional] 

### Return type

**object**

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

# **get_toolkit_oauth_status_tools_oauth_status_get**
> object get_toolkit_oauth_status_tools_oauth_status_get(project_id, toolkit_name, x_api_key=x_api_key, x_api_secret=x_api_secret)

Get Toolkit Oauth Status

Get OAuth authentication status for a toolkit

### Example


```python
import odin_sdk
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
    api_instance = odin_sdk.CustomToolsApi(api_client)
    project_id = 'project_id_example' # str | Project ID
    toolkit_name = 'toolkit_name_example' # str | Toolkit name
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Get Toolkit Oauth Status
        api_response = api_instance.get_toolkit_oauth_status_tools_oauth_status_get(project_id, toolkit_name, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of CustomToolsApi->get_toolkit_oauth_status_tools_oauth_status_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomToolsApi->get_toolkit_oauth_status_tools_oauth_status_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project ID | 
 **toolkit_name** | **str**| Toolkit name | 
 **x_api_key** | **str**| Your Odin API key. | [optional] 
 **x_api_secret** | **str**| Your Odin API secret. | [optional] 

### Return type

**object**

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

# **get_tools_schedule_status_batch_tools_custom_schedule_status_batch_post**
> object get_tools_schedule_status_batch_tools_custom_schedule_status_batch_post(request_body, x_api_key=x_api_key, x_api_secret=x_api_secret)

Get Tools Schedule Status Batch

Get schedule status for multiple custom tools/workflows in a single call

### Example


```python
import odin_sdk
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
    api_instance = odin_sdk.CustomToolsApi(api_client)
    request_body = ['request_body_example'] # List[Optional[str]] | 
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Get Tools Schedule Status Batch
        api_response = api_instance.get_tools_schedule_status_batch_tools_custom_schedule_status_batch_post(request_body, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of CustomToolsApi->get_tools_schedule_status_batch_tools_custom_schedule_status_batch_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomToolsApi->get_tools_schedule_status_batch_tools_custom_schedule_status_batch_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_body** | [**List[Optional[str]]**](str.md)|  | 
 **x_api_key** | **str**| Your Odin API key. | [optional] 
 **x_api_secret** | **str**| Your Odin API secret. | [optional] 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **import_custom_tool_tools_custom_import_post**
> CustomToolResponse import_custom_tool_tools_custom_import_post(import_tool_request, x_api_key=x_api_key, x_api_secret=x_api_secret)

Import Custom Tool

Import a custom tool from JSON

### Example


```python
import odin_sdk
from odin_sdk.models.custom_tool_response import CustomToolResponse
from odin_sdk.models.import_tool_request import ImportToolRequest
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
    api_instance = odin_sdk.CustomToolsApi(api_client)
    import_tool_request = odin_sdk.ImportToolRequest() # ImportToolRequest | 
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Import Custom Tool
        api_response = api_instance.import_custom_tool_tools_custom_import_post(import_tool_request, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of CustomToolsApi->import_custom_tool_tools_custom_import_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomToolsApi->import_custom_tool_tools_custom_import_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **import_tool_request** | [**ImportToolRequest**](ImportToolRequest.md)|  | 
 **x_api_key** | **str**| Your Odin API key. | [optional] 
 **x_api_secret** | **str**| Your Odin API secret. | [optional] 

### Return type

[**CustomToolResponse**](CustomToolResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pause_tool_schedule_tools_custom_tool_id_pause_schedule_post**
> object pause_tool_schedule_tools_custom_tool_id_pause_schedule_post(tool_id, x_api_key=x_api_key, x_api_secret=x_api_secret)

Pause Tool Schedule

Pause all schedule triggers for a tool

### Example


```python
import odin_sdk
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
    api_instance = odin_sdk.CustomToolsApi(api_client)
    tool_id = 'tool_id_example' # str | 
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Pause Tool Schedule
        api_response = api_instance.pause_tool_schedule_tools_custom_tool_id_pause_schedule_post(tool_id, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of CustomToolsApi->pause_tool_schedule_tools_custom_tool_id_pause_schedule_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomToolsApi->pause_tool_schedule_tools_custom_tool_id_pause_schedule_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tool_id** | **str**|  | 
 **x_api_key** | **str**| Your Odin API key. | [optional] 
 **x_api_secret** | **str**| Your Odin API secret. | [optional] 

### Return type

**object**

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

# **publish_custom_tool_tools_custom_tool_id_publish_post**
> CustomToolResponse publish_custom_tool_tools_custom_tool_id_publish_post(tool_id, publish_tool_request, x_api_key=x_api_key, x_api_secret=x_api_secret)

Publish Custom Tool

Publish a draft tool version

### Example


```python
import odin_sdk
from odin_sdk.models.custom_tool_response import CustomToolResponse
from odin_sdk.models.publish_tool_request import PublishToolRequest
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
    api_instance = odin_sdk.CustomToolsApi(api_client)
    tool_id = 'tool_id_example' # str | 
    publish_tool_request = odin_sdk.PublishToolRequest() # PublishToolRequest | 
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Publish Custom Tool
        api_response = api_instance.publish_custom_tool_tools_custom_tool_id_publish_post(tool_id, publish_tool_request, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of CustomToolsApi->publish_custom_tool_tools_custom_tool_id_publish_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomToolsApi->publish_custom_tool_tools_custom_tool_id_publish_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tool_id** | **str**|  | 
 **publish_tool_request** | [**PublishToolRequest**](PublishToolRequest.md)|  | 
 **x_api_key** | **str**| Your Odin API key. | [optional] 
 **x_api_secret** | **str**| Your Odin API secret. | [optional] 

### Return type

[**CustomToolResponse**](CustomToolResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **resume_tool_schedule_tools_custom_tool_id_resume_schedule_post**
> object resume_tool_schedule_tools_custom_tool_id_resume_schedule_post(tool_id, x_api_key=x_api_key, x_api_secret=x_api_secret)

Resume Tool Schedule

Resume all schedule triggers for a tool

### Example


```python
import odin_sdk
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
    api_instance = odin_sdk.CustomToolsApi(api_client)
    tool_id = 'tool_id_example' # str | 
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Resume Tool Schedule
        api_response = api_instance.resume_tool_schedule_tools_custom_tool_id_resume_schedule_post(tool_id, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of CustomToolsApi->resume_tool_schedule_tools_custom_tool_id_resume_schedule_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomToolsApi->resume_tool_schedule_tools_custom_tool_id_resume_schedule_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tool_id** | **str**|  | 
 **x_api_key** | **str**| Your Odin API key. | [optional] 
 **x_api_secret** | **str**| Your Odin API secret. | [optional] 

### Return type

**object**

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

# **revert_draft_to_version_tools_custom_tool_id_revert_to_version_post**
> CustomToolResponse revert_draft_to_version_tools_custom_tool_id_revert_to_version_post(tool_id, version, x_api_key=x_api_key, x_api_secret=x_api_secret)

Revert Draft To Version

Restore and publish a specific version (points back to that version)

### Example


```python
import odin_sdk
from odin_sdk.models.custom_tool_response import CustomToolResponse
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
    api_instance = odin_sdk.CustomToolsApi(api_client)
    tool_id = 'tool_id_example' # str | 
    version = 'version_example' # str | The version to restore and publish
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Revert Draft To Version
        api_response = api_instance.revert_draft_to_version_tools_custom_tool_id_revert_to_version_post(tool_id, version, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of CustomToolsApi->revert_draft_to_version_tools_custom_tool_id_revert_to_version_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomToolsApi->revert_draft_to_version_tools_custom_tool_id_revert_to_version_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tool_id** | **str**|  | 
 **version** | **str**| The version to restore and publish | 
 **x_api_key** | **str**| Your Odin API key. | [optional] 
 **x_api_secret** | **str**| Your Odin API secret. | [optional] 

### Return type

[**CustomToolResponse**](CustomToolResponse.md)

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

# **update_custom_tool_tools_custom_tool_id_put**
> CustomToolResponse update_custom_tool_tools_custom_tool_id_put(tool_id, update_custom_tool_request, x_api_key=x_api_key, x_api_secret=x_api_secret)

Update Custom Tool

Update a custom tool

### Example


```python
import odin_sdk
from odin_sdk.models.custom_tool_response import CustomToolResponse
from odin_sdk.models.update_custom_tool_request import UpdateCustomToolRequest
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
    api_instance = odin_sdk.CustomToolsApi(api_client)
    tool_id = 'tool_id_example' # str | 
    update_custom_tool_request = odin_sdk.UpdateCustomToolRequest() # UpdateCustomToolRequest | 
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Update Custom Tool
        api_response = api_instance.update_custom_tool_tools_custom_tool_id_put(tool_id, update_custom_tool_request, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of CustomToolsApi->update_custom_tool_tools_custom_tool_id_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomToolsApi->update_custom_tool_tools_custom_tool_id_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tool_id** | **str**|  | 
 **update_custom_tool_request** | [**UpdateCustomToolRequest**](UpdateCustomToolRequest.md)|  | 
 **x_api_key** | **str**| Your Odin API key. | [optional] 
 **x_api_secret** | **str**| Your Odin API secret. | [optional] 

### Return type

[**CustomToolResponse**](CustomToolResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

