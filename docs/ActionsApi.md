# odin_sdk.ActionsApi

All URIs are relative to *https://127.0.0.1:8001*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_tool_tools_api_post**](ActionsApi.md#api_tool_tools_api_post) | **POST** /tools/api | Api Tool
[**deploy_bot_tool_tools_deploy_bot_post**](ActionsApi.md#deploy_bot_tool_tools_deploy_bot_post) | **POST** /tools/deploy-bot | Deploy Bot Tool


# **api_tool_tools_api_post**
> ApiToolResponse api_tool_tools_api_post(api_tool_request, x_api_key=x_api_key, x_api_secret=x_api_secret)

Api Tool

Execute the API tool

### Example


```python
import odin_sdk
from odin_sdk.models.api_tool_request import ApiToolRequest
from odin_sdk.models.api_tool_response import ApiToolResponse
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
    api_instance = odin_sdk.ActionsApi(api_client)
    api_tool_request = odin_sdk.ApiToolRequest() # ApiToolRequest | 
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Api Tool
        api_response = api_instance.api_tool_tools_api_post(api_tool_request, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of ActionsApi->api_tool_tools_api_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActionsApi->api_tool_tools_api_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_tool_request** | [**ApiToolRequest**](ApiToolRequest.md)|  | 
 **x_api_key** | **str**| Your Odin API key. | [optional] 
 **x_api_secret** | **str**| Your Odin API secret. | [optional] 

### Return type

[**ApiToolResponse**](ApiToolResponse.md)

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

# **deploy_bot_tool_tools_deploy_bot_post**
> DeployBotToolResponse deploy_bot_tool_tools_deploy_bot_post(deploy_bot_tool_request, x_api_key=x_api_key, x_api_secret=x_api_secret)

Deploy Bot Tool

Execute the Deploy Bot tool

### Example


```python
import odin_sdk
from odin_sdk.models.deploy_bot_tool_request import DeployBotToolRequest
from odin_sdk.models.deploy_bot_tool_response import DeployBotToolResponse
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
    api_instance = odin_sdk.ActionsApi(api_client)
    deploy_bot_tool_request = odin_sdk.DeployBotToolRequest() # DeployBotToolRequest | 
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Deploy Bot Tool
        api_response = api_instance.deploy_bot_tool_tools_deploy_bot_post(deploy_bot_tool_request, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of ActionsApi->deploy_bot_tool_tools_deploy_bot_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActionsApi->deploy_bot_tool_tools_deploy_bot_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **deploy_bot_tool_request** | [**DeployBotToolRequest**](DeployBotToolRequest.md)|  | 
 **x_api_key** | **str**| Your Odin API key. | [optional] 
 **x_api_secret** | **str**| Your Odin API secret. | [optional] 

### Return type

[**DeployBotToolResponse**](DeployBotToolResponse.md)

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

