# TopicModelKeyword


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**keyword** | **object** |  | 
**current_count** | **object** |  | 
**min_count** | **object** |  | 
**max_count** | **object** |  | 

## Example

```python
from odin_sdk.models.topic_model_keyword import TopicModelKeyword

# TODO update the JSON string below
json = "{}"
# create an instance of TopicModelKeyword from a JSON string
topic_model_keyword_instance = TopicModelKeyword.from_json(json)
# print the JSON string representation of the object
print TopicModelKeyword.to_json()

# convert the object into a dict
topic_model_keyword_dict = topic_model_keyword_instance.to_dict()
# create an instance of TopicModelKeyword from a dict
topic_model_keyword_form_dict = topic_model_keyword.from_dict(topic_model_keyword_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


