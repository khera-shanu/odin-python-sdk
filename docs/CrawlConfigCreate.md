# CrawlConfigCreate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**crawl_name** | **object** |  | 
**root_url** | **object** |  | 
**repeat** | [**Repeat**](Repeat.md) |  | [optional] 
**limit_to_root_domain** | **object** |  | [optional] 
**limit_to_domains** | **object** |  | [optional] 
**limit_to_patterns** | **object** |  | [optional] 
**download_files** | **object** |  | [optional] 
**max_depth** | **object** |  | [optional] 
**max_pages** | **object** |  | [optional] 
**strategy** | **object** |  | [optional] 
**keywords_for_best_first** | **object** |  | [optional] 
**keywords_weight** | **object** |  | [optional] 

## Example

```python
from odin_sdk.models.crawl_config_create import CrawlConfigCreate

# TODO update the JSON string below
json = "{}"
# create an instance of CrawlConfigCreate from a JSON string
crawl_config_create_instance = CrawlConfigCreate.from_json(json)
# print the JSON string representation of the object
print CrawlConfigCreate.to_json()

# convert the object into a dict
crawl_config_create_dict = crawl_config_create_instance.to_dict()
# create an instance of CrawlConfigCreate from a dict
crawl_config_create_form_dict = crawl_config_create.from_dict(crawl_config_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


