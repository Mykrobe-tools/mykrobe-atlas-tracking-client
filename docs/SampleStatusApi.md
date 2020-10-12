# tracking_client.SampleStatusApi

All URIs are relative to *http://tracking-api-service/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**samples_id_status_delete**](SampleStatusApi.md#samples_id_status_delete) | **DELETE** /samples/{id}/status | 
[**samples_id_status_get**](SampleStatusApi.md#samples_id_status_get) | **GET** /samples/{id}/status | 
[**samples_id_status_patch**](SampleStatusApi.md#samples_id_status_patch) | **PATCH** /samples/{id}/status | 
[**samples_id_status_put**](SampleStatusApi.md#samples_id_status_put) | **PUT** /samples/{id}/status | 


# **samples_id_status_delete**
> samples_id_status_delete(id)



Delete the status associated with a sample with {id}.

### Example

```python
from __future__ import print_function
import time
import tracking_client
from tracking_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://tracking-api-service/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = tracking_client.Configuration(
    host = "http://tracking-api-service/api/v1"
)


# Enter a context with an instance of the API client
with tracking_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = tracking_client.SampleStatusApi(api_client)
    id = 'id_example' # str | 

    try:
        api_instance.samples_id_status_delete(id)
    except ApiException as e:
        print("Exception when calling SampleStatusApi->samples_id_status_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Deleted |  -  |
**404** | Not found |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **samples_id_status_get**
> Status samples_id_status_get(id)



Return the status associated with a sample.

### Example

```python
from __future__ import print_function
import time
import tracking_client
from tracking_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://tracking-api-service/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = tracking_client.Configuration(
    host = "http://tracking-api-service/api/v1"
)


# Enter a context with an instance of the API client
with tracking_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = tracking_client.SampleStatusApi(api_client)
    id = 'id_example' # str | 

    try:
        api_response = api_instance.samples_id_status_get(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SampleStatusApi->samples_id_status_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)|  | 

### Return type

[**Status**](Status.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | Not found |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **samples_id_status_patch**
> Status samples_id_status_patch(id, status)



Update status associated with a sample with new data.

### Example

```python
from __future__ import print_function
import time
import tracking_client
from tracking_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://tracking-api-service/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = tracking_client.Configuration(
    host = "http://tracking-api-service/api/v1"
)


# Enter a context with an instance of the API client
with tracking_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = tracking_client.SampleStatusApi(api_client)
    id = 'id_example' # str | 
status = tracking_client.Status() # Status | Status to be added

    try:
        api_response = api_instance.samples_id_status_patch(id, status)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SampleStatusApi->samples_id_status_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)|  | 
 **status** | [**Status**](Status.md)| Status to be added | 

### Return type

[**Status**](Status.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | Not found (sample not found) |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **samples_id_status_put**
> Status samples_id_status_put(id, status)



Add or replace new status associated with a sample.

### Example

```python
from __future__ import print_function
import time
import tracking_client
from tracking_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://tracking-api-service/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = tracking_client.Configuration(
    host = "http://tracking-api-service/api/v1"
)


# Enter a context with an instance of the API client
with tracking_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = tracking_client.SampleStatusApi(api_client)
    id = 'id_example' # str | 
status = tracking_client.Status() # Status | Status to be added.

    try:
        api_response = api_instance.samples_id_status_put(id, status)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SampleStatusApi->samples_id_status_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)|  | 
 **status** | [**Status**](Status.md)| Status to be added. | 

### Return type

[**Status**](Status.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  * Location - uri for the status <br>  |
**404** | Not found (sample not found) |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

