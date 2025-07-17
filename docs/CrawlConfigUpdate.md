# CrawlConfigUpdate


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
from odin_sdk.models.crawl_config_update import CrawlConfigUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of CrawlConfigUpdate from a JSON string
crawl_config_update_instance = CrawlConfigUpdate.from_json(json)
# print the JSON string representation of the object
print CrawlConfigUpdate.to_json()

# convert the object into a dict
crawl_config_update_dict = crawl_config_update_instance.to_dict()
# create an instance of CrawlConfigUpdate from a dict
crawl_config_update_form_dict = crawl_config_update.from_dict(crawl_config_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


