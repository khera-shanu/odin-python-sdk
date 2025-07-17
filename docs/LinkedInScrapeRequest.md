# LinkedInScrapeRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**query** | **object** | The query to search for on LinkedIn | 
**num_links** | **object** | The number of LinkedIn profiles to retrieve (default is 1) | [optional] 
**urls_to_exclude** | **object** | List of LinkedIn profile URLs to exclude (optional) | [optional] 

## Example

```python
from odin_sdk.models.linked_in_scrape_request import LinkedInScrapeRequest

# TODO update the JSON string below
json = "{}"
# create an instance of LinkedInScrapeRequest from a JSON string
linked_in_scrape_request_instance = LinkedInScrapeRequest.from_json(json)
# print the JSON string representation of the object
print LinkedInScrapeRequest.to_json()

# convert the object into a dict
linked_in_scrape_request_dict = linked_in_scrape_request_instance.to_dict()
# create an instance of LinkedInScrapeRequest from a dict
linked_in_scrape_request_form_dict = linked_in_scrape_request.from_dict(linked_in_scrape_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


