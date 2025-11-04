# odin_sdk.ScheduleManagementApi

All URIs are relative to *https://127.0.0.1:8001*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_tool_schedule_status_tools_custom_tool_id_schedule_status_get**](ScheduleManagementApi.md#get_tool_schedule_status_tools_custom_tool_id_schedule_status_get) | **GET** /tools/custom/{tool_id}/schedule-status | Get Tool Schedule Status
[**get_tools_schedule_status_batch_tools_custom_schedule_status_batch_post**](ScheduleManagementApi.md#get_tools_schedule_status_batch_tools_custom_schedule_status_batch_post) | **POST** /tools/custom/schedule-status/batch | Get Tools Schedule Status Batch
[**pause_tool_schedule_tools_custom_tool_id_pause_schedule_post**](ScheduleManagementApi.md#pause_tool_schedule_tools_custom_tool_id_pause_schedule_post) | **POST** /tools/custom/{tool_id}/pause-schedule | Pause Tool Schedule
[**resume_tool_schedule_tools_custom_tool_id_resume_schedule_post**](ScheduleManagementApi.md#resume_tool_schedule_tools_custom_tool_id_resume_schedule_post) | **POST** /tools/custom/{tool_id}/resume-schedule | Resume Tool Schedule


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
    api_instance = odin_sdk.ScheduleManagementApi(api_client)
    tool_id = 'tool_id_example' # str | 
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Get Tool Schedule Status
        api_response = api_instance.get_tool_schedule_status_tools_custom_tool_id_schedule_status_get(tool_id, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of ScheduleManagementApi->get_tool_schedule_status_tools_custom_tool_id_schedule_status_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ScheduleManagementApi->get_tool_schedule_status_tools_custom_tool_id_schedule_status_get: %s\n" % e)
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
    api_instance = odin_sdk.ScheduleManagementApi(api_client)
    request_body = ['request_body_example'] # List[Optional[str]] | 
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Get Tools Schedule Status Batch
        api_response = api_instance.get_tools_schedule_status_batch_tools_custom_schedule_status_batch_post(request_body, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of ScheduleManagementApi->get_tools_schedule_status_batch_tools_custom_schedule_status_batch_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ScheduleManagementApi->get_tools_schedule_status_batch_tools_custom_schedule_status_batch_post: %s\n" % e)
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
    api_instance = odin_sdk.ScheduleManagementApi(api_client)
    tool_id = 'tool_id_example' # str | 
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Pause Tool Schedule
        api_response = api_instance.pause_tool_schedule_tools_custom_tool_id_pause_schedule_post(tool_id, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of ScheduleManagementApi->pause_tool_schedule_tools_custom_tool_id_pause_schedule_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ScheduleManagementApi->pause_tool_schedule_tools_custom_tool_id_pause_schedule_post: %s\n" % e)
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
    api_instance = odin_sdk.ScheduleManagementApi(api_client)
    tool_id = 'tool_id_example' # str | 
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Resume Tool Schedule
        api_response = api_instance.resume_tool_schedule_tools_custom_tool_id_resume_schedule_post(tool_id, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of ScheduleManagementApi->resume_tool_schedule_tools_custom_tool_id_resume_schedule_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ScheduleManagementApi->resume_tool_schedule_tools_custom_tool_id_resume_schedule_post: %s\n" % e)
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

