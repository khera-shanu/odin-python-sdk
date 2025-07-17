# CrawlConfigResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **object** |  | 
**crawl_name** | **object** |  | 
**root_url** | **object** |  | 
**created_at** | **object** |  | 
**updated_at** | **object** |  | 
**project_id** | **object** |  | 
**user_id** | **object** |  | 
**repeat** | [**Repeat**](Repeat.md) |  | 
**limit_to_root_domain** | **object** |  | 
**limit_to_domains** | **object** |  | 
**limit_to_patterns** | **object** |  | 
**download_files** | **object** |  | 
**max_depth** | **object** |  | 
**max_pages** | **object** |  | 
**strategy** | **object** |  | 
**keywords_for_best_first** | **object** |  | 
**keywords_weight** | **object** |  | 

## Example

```python
from odin_sdk.models.crawl_config_response import CrawlConfigResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CrawlConfigResponse from a JSON string
crawl_config_response_instance = CrawlConfigResponse.from_json(json)
# print the JSON string representation of the object
print CrawlConfigResponse.to_json()

# convert the object into a dict
crawl_config_response_dict = crawl_config_response_instance.to_dict()
# create an instance of CrawlConfigResponse from a dict
crawl_config_response_form_dict = crawl_config_response.from_dict(crawl_config_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


