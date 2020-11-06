# tracking_client.SampleApi

All URIs are relative to *http://tracking-api-service/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**samples_get**](SampleApi.md#samples_get) | **GET** /samples | 
[**samples_id_get**](SampleApi.md#samples_id_get) | **GET** /samples/{id} | 
[**samples_id_head**](SampleApi.md#samples_id_head) | **HEAD** /samples/{id} | 
[**samples_id_patch**](SampleApi.md#samples_id_patch) | **PATCH** /samples/{id} | 
[**samples_post**](SampleApi.md#samples_post) | **POST** /samples | 


# **samples_get**
> list[Sample] samples_get(experiment_id=experiment_id, isolate_id=isolate_id)



Return a list of samples based on filtering parameters.

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
    api_instance = tracking_client.SampleApi(api_client)
    experiment_id = 'experiment_id_example' # str |  (optional)
isolate_id = 'isolate_id_example' # str |  (optional)

    try:
        api_response = api_instance.samples_get(experiment_id=experiment_id, isolate_id=isolate_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SampleApi->samples_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **experiment_id** | **str**|  | [optional] 
 **isolate_id** | **str**|  | [optional] 

### Return type

[**list[Sample]**](Sample.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **samples_id_get**
> Sample samples_id_get(id)



Return a sample by its ID.

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
    api_instance = tracking_client.SampleApi(api_client)
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
    api_instance = tracking_client.SampleApi(api_client)
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

# **samples_id_patch**
> Sample samples_id_patch(id, sample)



Update a sample.

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
    api_instance = tracking_client.SampleApi(api_client)
    id = 'id_example' # str | 
sample = tracking_client.Sample() # Sample | New properties for this sample

    try:
        api_response = api_instance.samples_id_patch(id, sample)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SampleApi->samples_id_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)|  | 
 **sample** | [**Sample**](Sample.md)| New properties for this sample | 

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
**200** | Updated |  -  |
**404** | Not found |  -  |
**409** | One or more of the unique properties lready existed |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **samples_post**
> Sample samples_post(sample)



Add a new sample.

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
    api_instance = tracking_client.SampleApi(api_client)
    sample = tracking_client.Sample() # Sample | Sample to be added

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

