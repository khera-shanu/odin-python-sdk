# odin_sdk.SecretsApi

All URIs are relative to *https://api.getodin.ai*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_secret_secrets_post**](SecretsApi.md#create_secret_secrets_post) | **POST** /secrets | Create Secret
[**delete_secret_secrets_secret_id_delete**](SecretsApi.md#delete_secret_secrets_secret_id_delete) | **DELETE** /secrets/{secret_id} | Delete Secret
[**get_secret_audit_logs_secrets_secret_id_audit_get**](SecretsApi.md#get_secret_audit_logs_secrets_secret_id_audit_get) | **GET** /secrets/{secret_id}/audit | Get Secret Audit Logs
[**get_secret_secrets_secret_id_get**](SecretsApi.md#get_secret_secrets_secret_id_get) | **GET** /secrets/{secret_id} | Get Secret
[**get_secrets_secrets_get**](SecretsApi.md#get_secrets_secrets_get) | **GET** /secrets | Get Secrets
[**update_secret_secrets_secret_id_put**](SecretsApi.md#update_secret_secrets_secret_id_put) | **PUT** /secrets/{secret_id} | Update Secret


# **create_secret_secrets_post**
> SecretResponse create_secret_secrets_post(secret_create, x_api_key=x_api_key, x_api_secret=x_api_secret)

Create Secret

Create a new secret. Only admin users can access this endpoint.

### Example


```python
import time
import os
import odin_sdk
from odin_sdk.models.secret_create import SecretCreate
from odin_sdk.models.secret_response import SecretResponse
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
    api_instance = odin_sdk.SecretsApi(api_client)
    secret_create = odin_sdk.SecretCreate() # SecretCreate | 
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Create Secret
        api_response = api_instance.create_secret_secrets_post(secret_create, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of SecretsApi->create_secret_secrets_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SecretsApi->create_secret_secrets_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **secret_create** | [**SecretCreate**](SecretCreate.md)|  | 
 **x_api_key** | **str**| Your Odin API key. | [optional] 
 **x_api_secret** | **str**| Your Odin API secret. | [optional] 

### Return type

[**SecretResponse**](SecretResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Successful Response |  -  |
**401** | Unauthorized |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_secret_secrets_secret_id_delete**
> SuccessResponse delete_secret_secrets_secret_id_delete(secret_id, soft=soft, x_api_key=x_api_key, x_api_secret=x_api_secret)

Delete Secret

Delete a secret. Only admin users can access this endpoint. When soft=True (default), the secret is marked as deleted but remains in the database. When soft=False, the secret is permanently removed.

### Example


```python
import time
import os
import odin_sdk
from odin_sdk.models.success_response import SuccessResponse
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
    api_instance = odin_sdk.SecretsApi(api_client)
    secret_id = None # object | ID of the secret to delete
    soft = None # object | Use soft delete (mark as deleted) instead of hard delete (remove permanently) (optional)
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Delete Secret
        api_response = api_instance.delete_secret_secrets_secret_id_delete(secret_id, soft=soft, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of SecretsApi->delete_secret_secrets_secret_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SecretsApi->delete_secret_secrets_secret_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **secret_id** | [**object**](.md)| ID of the secret to delete | 
 **soft** | [**object**](.md)| Use soft delete (mark as deleted) instead of hard delete (remove permanently) | [optional] 
 **x_api_key** | **str**| Your Odin API key. | [optional] 
 **x_api_secret** | **str**| Your Odin API secret. | [optional] 

### Return type

[**SuccessResponse**](SuccessResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**401** | Unauthorized |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_secret_audit_logs_secrets_secret_id_audit_get**
> PaginatedAuditLogsResponse get_secret_audit_logs_secrets_secret_id_audit_get(secret_id, action=action, start_date=start_date, end_date=end_date, page=page, limit=limit, x_api_key=x_api_key, x_api_secret=x_api_secret)

Get Secret Audit Logs

Retrieve audit logs for a specific secret. Only admin users can access this endpoint.

### Example


```python
import time
import os
import odin_sdk
from odin_sdk.models.paginated_audit_logs_response import PaginatedAuditLogsResponse
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
    api_instance = odin_sdk.SecretsApi(api_client)
    secret_id = None # object | ID of the secret
    action = odin_sdk.Action1() # Action1 |  (optional)
    start_date = odin_sdk.StartDate1() # StartDate1 | Filter logs from this date (ISO 8601 format) (optional)
    end_date = odin_sdk.EndDate1() # EndDate1 | Filter logs until this date (ISO 8601 format) (optional)
    page = None # object |  (optional)
    limit = None # object |  (optional)
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Get Secret Audit Logs
        api_response = api_instance.get_secret_audit_logs_secrets_secret_id_audit_get(secret_id, action=action, start_date=start_date, end_date=end_date, page=page, limit=limit, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of SecretsApi->get_secret_audit_logs_secrets_secret_id_audit_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SecretsApi->get_secret_audit_logs_secrets_secret_id_audit_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **secret_id** | [**object**](.md)| ID of the secret | 
 **action** | [**Action1**](.md)|  | [optional] 
 **start_date** | [**StartDate1**](.md)| Filter logs from this date (ISO 8601 format) | [optional] 
 **end_date** | [**EndDate1**](.md)| Filter logs until this date (ISO 8601 format) | [optional] 
 **page** | [**object**](.md)|  | [optional] 
 **limit** | [**object**](.md)|  | [optional] 
 **x_api_key** | **str**| Your Odin API key. | [optional] 
 **x_api_secret** | **str**| Your Odin API secret. | [optional] 

### Return type

[**PaginatedAuditLogsResponse**](PaginatedAuditLogsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**401** | Unauthorized |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_secret_secrets_secret_id_get**
> SecretResponse get_secret_secrets_secret_id_get(secret_id, include_deleted=include_deleted, x_api_key=x_api_key, x_api_secret=x_api_secret)

Get Secret

Retrieve a specific secret by ID. Only admin users can access this endpoint.

### Example


```python
import time
import os
import odin_sdk
from odin_sdk.models.secret_response import SecretResponse
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
    api_instance = odin_sdk.SecretsApi(api_client)
    secret_id = None # object | ID of the secret to retrieve
    include_deleted = None # object | Include soft-deleted secrets (optional)
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Get Secret
        api_response = api_instance.get_secret_secrets_secret_id_get(secret_id, include_deleted=include_deleted, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of SecretsApi->get_secret_secrets_secret_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SecretsApi->get_secret_secrets_secret_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **secret_id** | [**object**](.md)| ID of the secret to retrieve | 
 **include_deleted** | [**object**](.md)| Include soft-deleted secrets | [optional] 
 **x_api_key** | **str**| Your Odin API key. | [optional] 
 **x_api_secret** | **str**| Your Odin API secret. | [optional] 

### Return type

[**SecretResponse**](SecretResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**401** | Unauthorized |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_secrets_secrets_get**
> PaginatedSecretsResponse get_secrets_secrets_get(search=search, page=page, limit=limit, sort=sort, order=order, include_deleted=include_deleted, x_api_key=x_api_key, x_api_secret=x_api_secret)

Get Secrets

Retrieve a list of all secrets accessible to the current user. Only admin users can access this endpoint.

### Example


```python
import time
import os
import odin_sdk
from odin_sdk.models.paginated_secrets_response import PaginatedSecretsResponse
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
    api_instance = odin_sdk.SecretsApi(api_client)
    search = odin_sdk.Search1() # Search1 |  (optional)
    page = None # object |  (optional)
    limit = None # object |  (optional)
    sort = None # object |  (optional)
    order = None # object |  (optional)
    include_deleted = None # object | Include soft-deleted secrets in results (optional)
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Get Secrets
        api_response = api_instance.get_secrets_secrets_get(search=search, page=page, limit=limit, sort=sort, order=order, include_deleted=include_deleted, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of SecretsApi->get_secrets_secrets_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SecretsApi->get_secrets_secrets_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search** | [**Search1**](.md)|  | [optional] 
 **page** | [**object**](.md)|  | [optional] 
 **limit** | [**object**](.md)|  | [optional] 
 **sort** | [**object**](.md)|  | [optional] 
 **order** | [**object**](.md)|  | [optional] 
 **include_deleted** | [**object**](.md)| Include soft-deleted secrets in results | [optional] 
 **x_api_key** | **str**| Your Odin API key. | [optional] 
 **x_api_secret** | **str**| Your Odin API secret. | [optional] 

### Return type

[**PaginatedSecretsResponse**](PaginatedSecretsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**401** | Unauthorized |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_secret_secrets_secret_id_put**
> SecretResponse update_secret_secrets_secret_id_put(secret_id, secret_update, x_api_key=x_api_key, x_api_secret=x_api_secret)

Update Secret

Update an existing secret. Only admin users can access this endpoint.

### Example


```python
import time
import os
import odin_sdk
from odin_sdk.models.secret_response import SecretResponse
from odin_sdk.models.secret_update import SecretUpdate
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
    api_instance = odin_sdk.SecretsApi(api_client)
    secret_id = None # object | ID of the secret to update
    secret_update = odin_sdk.SecretUpdate() # SecretUpdate | 
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Update Secret
        api_response = api_instance.update_secret_secrets_secret_id_put(secret_id, secret_update, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of SecretsApi->update_secret_secrets_secret_id_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SecretsApi->update_secret_secrets_secret_id_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **secret_id** | [**object**](.md)| ID of the secret to update | 
 **secret_update** | [**SecretUpdate**](SecretUpdate.md)|  | 
 **x_api_key** | **str**| Your Odin API key. | [optional] 
 **x_api_secret** | **str**| Your Odin API secret. | [optional] 

### Return type

[**SecretResponse**](SecretResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**401** | Unauthorized |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

