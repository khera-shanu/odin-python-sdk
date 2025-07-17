# GetChatAnalyticsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start_date** | [**StartDate4**](StartDate4.md) |  | [optional] 
**end_date** | [**EndDate4**](EndDate4.md) |  | [optional] 

## Example

```python
from odin_sdk.models.get_chat_analytics_request import GetChatAnalyticsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GetChatAnalyticsRequest from a JSON string
get_chat_analytics_request_instance = GetChatAnalyticsRequest.from_json(json)
# print the JSON string representation of the object
print GetChatAnalyticsRequest.to_json()

# convert the object into a dict
get_chat_analytics_request_dict = get_chat_analytics_request_instance.to_dict()
# create an instance of GetChatAnalyticsRequest from a dict
get_chat_analytics_request_form_dict = get_chat_analytics_request.from_dict(get_chat_analytics_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


