# KnowledgeBaseAnalyticsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_messages** | **object** |  | 
**total_responses** | **object** |  | 
**failed_messages** | **object** |  | 
**avg_messages_per_user** | **object** |  | 
**avg_message_length** | **object** |  | 
**avg_response_length** | **object** |  | 
**avg_message_per_convo** | **object** |  | 
**positive_feedback** | **object** |  | 
**negative_feedback** | **object** |  | 
**similar_messages** | [**Dict[str, MessageGroup]**](MessageGroup.md) |  | 

## Example

```python
from odin_sdk.models.knowledge_base_analytics_response import KnowledgeBaseAnalyticsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of KnowledgeBaseAnalyticsResponse from a JSON string
knowledge_base_analytics_response_instance = KnowledgeBaseAnalyticsResponse.from_json(json)
# print the JSON string representation of the object
print KnowledgeBaseAnalyticsResponse.to_json()

# convert the object into a dict
knowledge_base_analytics_response_dict = knowledge_base_analytics_response_instance.to_dict()
# create an instance of KnowledgeBaseAnalyticsResponse from a dict
knowledge_base_analytics_response_form_dict = knowledge_base_analytics_response.from_dict(knowledge_base_analytics_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


