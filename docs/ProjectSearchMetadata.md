# ProjectSearchMetadata


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
from odin_sdk.models.project_search_metadata import ProjectSearchMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectSearchMetadata from a JSON string
project_search_metadata_instance = ProjectSearchMetadata.from_json(json)
# print the JSON string representation of the object
print ProjectSearchMetadata.to_json()

# convert the object into a dict
project_search_metadata_dict = project_search_metadata_instance.to_dict()
# create an instance of ProjectSearchMetadata from a dict
project_search_metadata_form_dict = project_search_metadata.from_dict(project_search_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


