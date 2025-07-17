# GoogleSearchArticlesRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**query** | **object** | The query to search for. | 
**max_results** | **object** | The maximum number of results to return. | [optional] 
**download_pages** | **object** | Whether to download the pages or not. | [optional] 
**search_type** | **object** | The search type. Currently all or news is supported. | [optional] 
**website_white_list** | **object** | The list of websites to limit the search to. | [optional] 
**limit_date_range** | [**LimitDateRange**](LimitDateRange.md) |  | [optional] 
**date_range_start** | [**DateRangeStart**](DateRangeStart.md) |  | [optional] 
**date_range_end** | [**DateRangeEnd**](DateRangeEnd.md) |  | [optional] 

## Example

```python
from odin_sdk.models.google_search_articles_request import GoogleSearchArticlesRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GoogleSearchArticlesRequest from a JSON string
google_search_articles_request_instance = GoogleSearchArticlesRequest.from_json(json)
# print the JSON string representation of the object
print GoogleSearchArticlesRequest.to_json()

# convert the object into a dict
google_search_articles_request_dict = google_search_articles_request_instance.to_dict()
# create an instance of GoogleSearchArticlesRequest from a dict
google_search_articles_request_form_dict = google_search_articles_request.from_dict(google_search_articles_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


