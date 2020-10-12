# tracking_client.EventApi

All URIs are relative to *http://tracking-api-service/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**samples_id_events_event_id_delete**](EventApi.md#samples_id_events_event_id_delete) | **DELETE** /samples/{id}/events/{eventId} | 
[**samples_id_events_event_id_get**](EventApi.md#samples_id_events_event_id_get) | **GET** /samples/{id}/events/{eventId} | 
[**samples_id_events_get**](EventApi.md#samples_id_events_get) | **GET** /samples/{id}/events | 
[**samples_id_events_post**](EventApi.md#samples_id_events_post) | **POST** /samples/{id}/events | 


# **samples_id_events_event_id_delete**
> samples_id_events_event_id_delete(id, event_id)



Delete an event with {eventId} associated with a sample with {id}.

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
    api_instance = tracking_client.EventApi(api_client)
    id = 'id_example' # str | 
event_id = 'event_id_example' # str | 

    try:
        api_instance.samples_id_events_event_id_delete(id, event_id)
    except ApiException as e:
        print("Exception when calling EventApi->samples_id_events_event_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)|  | 
 **event_id** | **str**|  | 

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

# **samples_id_events_event_id_get**
> Event samples_id_events_event_id_get(id, event_id)



Return an event with {eventId} associated with a sample with {id}.

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
    api_instance = tracking_client.EventApi(api_client)
    id = 'id_example' # str | 
event_id = 'event_id_example' # str | 

    try:
        api_response = api_instance.samples_id_events_event_id_get(id, event_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling EventApi->samples_id_events_event_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)|  | 
 **event_id** | **str**|  | 

### Return type

[**Event**](Event.md)

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

# **samples_id_events_get**
> list[Event] samples_id_events_get(id)



Return a list of events associated with a sample.

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
    api_instance = tracking_client.EventApi(api_client)
    id = 'id_example' # str | 

    try:
        api_response = api_instance.samples_id_events_get(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling EventApi->samples_id_events_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)|  | 

### Return type

[**list[Event]**](Event.md)

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

# **samples_id_events_post**
> Event samples_id_events_post(id, event)



Add a new event to be associated with a sample.

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
    api_instance = tracking_client.EventApi(api_client)
    id = 'id_example' # str | 
event = tracking_client.Event() # Event | Event to be added

    try:
        api_response = api_instance.samples_id_events_post(id, event)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling EventApi->samples_id_events_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)|  | 
 **event** | [**Event**](Event.md)| Event to be added | 

### Return type

[**Event**](Event.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  * Location - uri for the newly added event <br>  |
**404** | Not found (sample not found) |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

