# openapi_client.SampleApi

All URIs are relative to *http://tracking-api-service/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**samples_id_get**](SampleApi.md#samples_id_get) | **GET** /samples/{id} | 
[**samples_id_head**](SampleApi.md#samples_id_head) | **HEAD** /samples/{id} | 
[**samples_post**](SampleApi.md#samples_post) | **POST** /samples | 


# **samples_id_get**
> Sample samples_id_get(id)



Return a sample by its ID.

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
    api_instance = openapi_client.SampleApi(api_client)
    id = 'id_example' # str | 

    try:
        api_response = api_instance.samples_id_get(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SampleApi->samples_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)|  | 

### Return type

[**Sample**](Sample.md)

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

# **samples_id_head**
> samples_id_head(id)



Return if a sample with {id} exists.

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
    api_instance = openapi_client.SampleApi(api_client)
    id = 'id_example' # str | 

    try:
        api_instance.samples_id_head(id)
    except ApiException as e:
        print("Exception when calling SampleApi->samples_id_head: %s\n" % e)
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
**204** | OK |  -  |
**404** | Not found |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **samples_post**
> Sample samples_post(sample)



Add a new sample.

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
    api_instance = openapi_client.SampleApi(api_client)
    sample = openapi_client.Sample() # Sample | Sample to be added

    try:
        api_response = api_instance.samples_post(sample)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SampleApi->samples_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sample** | [**Sample**](Sample.md)| Sample to be added | 

### Return type

[**Sample**](Sample.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  * Location - uri for the newly added sample <br>  |
**409** | Already existed |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

