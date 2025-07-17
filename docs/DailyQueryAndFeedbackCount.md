# DailyQueryAndFeedbackCount


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**day** | **object** |  | 
**month** | **object** |  | 
**year** | **object** |  | 
**query_count** | **object** |  | 
**upvoted_count** | **object** |  | 
**downvoted_count** | **object** |  | 
**feedbacks_stats** | [**DailyFeedbackStat**](DailyFeedbackStat.md) |  | 

## Example

```python
from odin_sdk.models.daily_query_and_feedback_count import DailyQueryAndFeedbackCount

# TODO update the JSON string below
json = "{}"
# create an instance of DailyQueryAndFeedbackCount from a JSON string
daily_query_and_feedback_count_instance = DailyQueryAndFeedbackCount.from_json(json)
# print the JSON string representation of the object
print DailyQueryAndFeedbackCount.to_json()

# convert the object into a dict
daily_query_and_feedback_count_dict = daily_query_and_feedback_count_instance.to_dict()
# create an instance of DailyQueryAndFeedbackCount from a dict
daily_query_and_feedback_count_form_dict = daily_query_and_feedback_count.from_dict(daily_query_and_feedback_count_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


