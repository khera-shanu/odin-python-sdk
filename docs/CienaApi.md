# odin_sdk.CienaApi

All URIs are relative to *https://api.getodin.ai*

Method | HTTP request | Description
------------- | ------------- | -------------
[**process_company_ciena_process_kaleidoscope_documents_post**](CienaApi.md#process_company_ciena_process_kaleidoscope_documents_post) | **POST** /ciena/process-kaleidoscope-documents | Process Company


# **process_company_ciena_process_kaleidoscope_documents_post**
> ProcessCompanyResponse process_company_ciena_process_kaleidoscope_documents_post(company_process_request)

Process Company

Process SEC filings for a company using Kaleidoscope.  This endpoint handles the processing of SEC filings for a specified company, including authentication and integration with the Kaleidoscope API.  Args:     request (CompanyProcessRequest): The complete request containing company and authentication details.  Returns:     ProcessCompanyResponse: Details about the processed filings and operation status.  Raises:     HTTPException:         - 400: If invalid parameters are provided         - 500: If there's an internal server error during processing

### Example


```python
import time
import os
import odin_sdk
from odin_sdk.models.company_process_request import CompanyProcessRequest
from odin_sdk.models.process_company_response import ProcessCompanyResponse
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
    api_instance = odin_sdk.CienaApi(api_client)
    company_process_request = odin_sdk.CompanyProcessRequest() # CompanyProcessRequest | 

    try:
        # Process Company
        api_response = api_instance.process_company_ciena_process_kaleidoscope_documents_post(company_process_request)
        print("The response of CienaApi->process_company_ciena_process_kaleidoscope_documents_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CienaApi->process_company_ciena_process_kaleidoscope_documents_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_process_request** | [**CompanyProcessRequest**](CompanyProcessRequest.md)|  | 

### Return type

[**ProcessCompanyResponse**](ProcessCompanyResponse.md)

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

