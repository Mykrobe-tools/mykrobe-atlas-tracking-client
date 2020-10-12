# openapi_client.QcResultApi

All URIs are relative to *http://tracking-api-service/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**samples_id_qc_result_delete**](QcResultApi.md#samples_id_qc_result_delete) | **DELETE** /samples/{id}/qc-result | 
[**samples_id_qc_result_get**](QcResultApi.md#samples_id_qc_result_get) | **GET** /samples/{id}/qc-result | 
[**samples_id_qc_result_put**](QcResultApi.md#samples_id_qc_result_put) | **PUT** /samples/{id}/qc-result | 


# **samples_id_qc_result_delete**
> samples_id_qc_result_delete(id)



Delete the QC result associated with a sample with {id}.

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://tracking-api-service/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://tracking-api-service/api/v1"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.QcResultApi(api_client)
    id = 'id_example' # str | 

    try:
        api_instance.samples_id_qc_result_delete(id)
    except ApiException as e:
        print("Exception when calling QcResultApi->samples_id_qc_result_delete: %s\n" % e)
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

# **samples_id_qc_result_get**
> QcResult samples_id_qc_result_get(id)



Return the QC result associated with a sample.

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://tracking-api-service/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://tracking-api-service/api/v1"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.QcResultApi(api_client)
    id = 'id_example' # str | 

    try:
        api_response = api_instance.samples_id_qc_result_get(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling QcResultApi->samples_id_qc_result_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)|  | 

### Return type

[**QcResult**](QcResult.md)

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

# **samples_id_qc_result_put**
> QcResult samples_id_qc_result_put(id, qc_result)



Add or replace new QC result associated with a sample.

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://tracking-api-service/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://tracking-api-service/api/v1"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.QcResultApi(api_client)
    id = 'id_example' # str | 
qc_result = openapi_client.QcResult() # QcResult | QC result to be added

    try:
        api_response = api_instance.samples_id_qc_result_put(id, qc_result)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling QcResultApi->samples_id_qc_result_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)|  | 
 **qc_result** | [**QcResult**](QcResult.md)| QC result to be added | 

### Return type

[**QcResult**](QcResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  * Location - uri for the QC result <br>  |
**404** | Not found (sample not found) |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

