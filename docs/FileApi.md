# tracking_client.FileApi

All URIs are relative to *http://tracking-api-service/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**files_md5sum_get**](FileApi.md#files_md5sum_get) | **GET** /files/{md5sum} | 
[**samples_id_files_get**](FileApi.md#samples_id_files_get) | **GET** /samples/{id}/files | 
[**samples_id_files_md5sum_delete**](FileApi.md#samples_id_files_md5sum_delete) | **DELETE** /samples/{id}/files/{md5sum} | 
[**samples_id_files_md5sum_get**](FileApi.md#samples_id_files_md5sum_get) | **GET** /samples/{id}/files/{md5sum} | 
[**samples_id_files_post**](FileApi.md#samples_id_files_post) | **POST** /samples/{id}/files | 


# **files_md5sum_get**
> File files_md5sum_get(md5sum)



Return a file based on a file md5sum.

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
    api_instance = tracking_client.FileApi(api_client)
    md5sum = 'md5sum_example' # str | 

    try:
        api_response = api_instance.files_md5sum_get(md5sum)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling FileApi->files_md5sum_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **md5sum** | **str**|  | 

### Return type

[**File**](File.md)

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

# **samples_id_files_get**
> list[File] samples_id_files_get(id)



Return a list of files associated with a sample.

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
    api_instance = tracking_client.FileApi(api_client)
    id = 'id_example' # str | 

    try:
        api_response = api_instance.samples_id_files_get(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling FileApi->samples_id_files_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)|  | 

### Return type

[**list[File]**](File.md)

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

# **samples_id_files_md5sum_delete**
> samples_id_files_md5sum_delete(id, md5sum)



Delete a file with {md5sum} associated with a sample with {id}.

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
    api_instance = tracking_client.FileApi(api_client)
    id = 'id_example' # str | 
md5sum = 'md5sum_example' # str | 

    try:
        api_instance.samples_id_files_md5sum_delete(id, md5sum)
    except ApiException as e:
        print("Exception when calling FileApi->samples_id_files_md5sum_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)|  | 
 **md5sum** | **str**|  | 

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

# **samples_id_files_md5sum_get**
> File samples_id_files_md5sum_get(id, md5sum)



Return a file with {md5sum} associated with a sample with {id}.

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
    api_instance = tracking_client.FileApi(api_client)
    id = 'id_example' # str | 
md5sum = 'md5sum_example' # str | 

    try:
        api_response = api_instance.samples_id_files_md5sum_get(id, md5sum)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling FileApi->samples_id_files_md5sum_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)|  | 
 **md5sum** | **str**|  | 

### Return type

[**File**](File.md)

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

# **samples_id_files_post**
> File samples_id_files_post(id, file)



Add a new file to be associated with a sample.

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
    api_instance = tracking_client.FileApi(api_client)
    id = 'id_example' # str | 
file = '/path/to/file' # File | File to be added

    try:
        api_response = api_instance.samples_id_files_post(id, file)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling FileApi->samples_id_files_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)|  | 
 **file** | [**File**](File.md)| File to be added | 

### Return type

[**File**](File.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  * Location - uri for the newly added file <br>  |
**404** | Not found (sample not found) |  -  |
**409** | Already existed (with same md5sum) |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

