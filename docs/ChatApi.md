# odin_sdk.ChatApi

All URIs are relative to *https://api.getodin.ai*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_default_models_chat_models_get**](ChatApi.md#get_default_models_chat_models_get) | **GET** /chat/models | Get Default Models


# **get_default_models_chat_models_get**
> ChatModelInfoResponse get_default_models_chat_models_get()

Get Default Models

Retrieves the list of default models available for the app.

### Example


```python
import time
import os
import odin_sdk
from odin_sdk.models.chat_model_info_response import ChatModelInfoResponse
from odin_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.getodin.ai
# See configuration.py for a list of all supported configuration parameters.
configuration = odin_sdk.Configuration(
    host = "https://api.getodin.ai"
)


# Enter a context with an instance of the API client
with odin_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = odin_sdk.ChatApi(api_client)

    try:
        # Get Default Models
        api_response = api_instance.get_default_models_chat_models_get()
        print("The response of ChatApi->get_default_models_chat_models_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ChatApi->get_default_models_chat_models_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**ChatModelInfoResponse**](ChatModelInfoResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

