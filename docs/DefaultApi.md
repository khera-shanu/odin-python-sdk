# odin_sdk.DefaultApi

All URIs are relative to *https://127.0.0.1:8001*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_youtube_captions_json_tools_ai_extract_youtube_captions_post**](DefaultApi.md#get_youtube_captions_json_tools_ai_extract_youtube_captions_post) | **POST** /tools/ai/extract-youtube-captions | Get Youtube Captions Json
[**sse_endpoint_tools_push_get**](DefaultApi.md#sse_endpoint_tools_push_get) | **GET** /tools/push | Sse Endpoint


# **get_youtube_captions_json_tools_ai_extract_youtube_captions_post**
> object get_youtube_captions_json_tools_ai_extract_youtube_captions_post(extract_youtube_captions_request)

Get Youtube Captions Json

### Example


```python
import odin_sdk
from odin_sdk.models.extract_youtube_captions_request import ExtractYoutubeCaptionsRequest
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
    api_instance = odin_sdk.DefaultApi(api_client)
    extract_youtube_captions_request = odin_sdk.ExtractYoutubeCaptionsRequest() # ExtractYoutubeCaptionsRequest | 

    try:
        # Get Youtube Captions Json
        api_response = api_instance.get_youtube_captions_json_tools_ai_extract_youtube_captions_post(extract_youtube_captions_request)
        print("The response of DefaultApi->get_youtube_captions_json_tools_ai_extract_youtube_captions_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_youtube_captions_json_tools_ai_extract_youtube_captions_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **extract_youtube_captions_request** | [**ExtractYoutubeCaptionsRequest**](ExtractYoutubeCaptionsRequest.md)|  | 

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

# **sse_endpoint_tools_push_get**
> object sse_endpoint_tools_push_get(push_ref)

Sse Endpoint

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
    api_instance = odin_sdk.DefaultApi(api_client)
    push_ref = 'push_ref_example' # str | 

    try:
        # Sse Endpoint
        api_response = api_instance.sse_endpoint_tools_push_get(push_ref)
        print("The response of DefaultApi->sse_endpoint_tools_push_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->sse_endpoint_tools_push_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **push_ref** | **str**|  | 

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

