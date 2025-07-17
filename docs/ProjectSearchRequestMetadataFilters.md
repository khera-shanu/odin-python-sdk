# ProjectSearchRequestMetadataFilters


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**doc_type** | [**DocType**](DocType.md) |  | [optional] 
**upload_date** | [**UploadDate1**](UploadDate1.md) |  | [optional] 
**entity_names** | [**EntityNames**](EntityNames.md) |  | [optional] 
**entity_types** | [**EntityTypes**](EntityTypes.md) |  | [optional] 
**entity_salience** | [**EntitySalience**](EntitySalience.md) |  | [optional] 
**entity_readability** | [**EntityReadability**](EntityReadability.md) |  | [optional] 

## Example

```python
from odin_sdk.models.project_search_request_metadata_filters import ProjectSearchRequestMetadataFilters

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectSearchRequestMetadataFilters from a JSON string
project_search_request_metadata_filters_instance = ProjectSearchRequestMetadataFilters.from_json(json)
# print the JSON string representation of the object
print ProjectSearchRequestMetadataFilters.to_json()

# convert the object into a dict
project_search_request_metadata_filters_dict = project_search_request_metadata_filters_instance.to_dict()
# create an instance of ProjectSearchRequestMetadataFilters from a dict
project_search_request_metadata_filters_form_dict = project_search_request_metadata_filters.from_dict(project_search_request_metadata_filters_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


