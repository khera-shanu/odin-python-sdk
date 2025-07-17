# GetChatAnalyticsResponseMetrics


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**average_response_time** | **object** |  | 
**average_queries_per_chat** | **object** |  | 
**average_query_token_count** | **object** |  | 
**average_response_token_count** | **object** |  | 
**total_upvotes** | **object** |  | 
**total_downvotes** | **object** |  | 
**total_messages** | **object** |  | 
**average_images_generated** | **object** |  | 
**total_document_usage** | **object** |  | 
**total_kb_search** | **object** |  | 
**total_images_generated** | **object** |  | 
**top_keywords** | **object** |  | 
**top_questions** | **object** |  | 
**regenerated_requests** | **object** |  | 
**users_message_counts** | **object** |  | 
**top_documents** | **object** |  | 

## Example

```python
from odin_sdk.models.get_chat_analytics_response_metrics import GetChatAnalyticsResponseMetrics

# TODO update the JSON string below
json = "{}"
# create an instance of GetChatAnalyticsResponseMetrics from a JSON string
get_chat_analytics_response_metrics_instance = GetChatAnalyticsResponseMetrics.from_json(json)
# print the JSON string representation of the object
print GetChatAnalyticsResponseMetrics.to_json()

# convert the object into a dict
get_chat_analytics_response_metrics_dict = get_chat_analytics_response_metrics_instance.to_dict()
# create an instance of GetChatAnalyticsResponseMetrics from a dict
get_chat_analytics_response_metrics_form_dict = get_chat_analytics_response_metrics.from_dict(get_chat_analytics_response_metrics_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


