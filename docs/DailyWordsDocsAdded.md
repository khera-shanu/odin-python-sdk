# DailyWordsDocsAdded


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**day** | **object** |  | 
**month** | **object** |  | 
**year** | **object** |  | 
**words_added** | **object** |  | 
**docs_added** | **object** |  | 

## Example

```python
from odin_sdk.models.daily_words_docs_added import DailyWordsDocsAdded

# TODO update the JSON string below
json = "{}"
# create an instance of DailyWordsDocsAdded from a JSON string
daily_words_docs_added_instance = DailyWordsDocsAdded.from_json(json)
# print the JSON string representation of the object
print DailyWordsDocsAdded.to_json()

# convert the object into a dict
daily_words_docs_added_dict = daily_words_docs_added_instance.to_dict()
# create an instance of DailyWordsDocsAdded from a dict
daily_words_docs_added_form_dict = daily_words_docs_added.from_dict(daily_words_docs_added_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


