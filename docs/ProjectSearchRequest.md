# ProjectSearchRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | **object** |  | 
**query** | **object** |  | 
**document_keys** | [**DocumentKeys2**](DocumentKeys2.md) |  | [optional] 
**hybrid_search_lambda** | **object** |  | [optional] 
**score_threshold** | **object** |  | [optional] 
**kw_fuzzy_threshold** | **object** |  | [optional] 
**kw_curve_multihit** | [**KwCurveMultihit**](KwCurveMultihit.md) |  | [optional] 
**metadata_filters** | [**ProjectSearchRequestMetadataFilters**](ProjectSearchRequestMetadataFilters.md) |  | [optional] 
**max_results** | [**MaxResults**](MaxResults.md) |  | [optional] 
**full_content_words_limit** | [**FullContentWordsLimit**](FullContentWordsLimit.md) |  | [optional] 
**metadata_weighting** | [**MetadataWeighting**](MetadataWeighting.md) |  | [optional] 
**remove_duplicates** | [**RemoveDuplicates**](RemoveDuplicates.md) |  | [optional] 
**page** | [**Page**](Page.md) |  | [optional] 
**debug** | [**Debug**](Debug.md) |  | [optional] 
**generate_ai_summary** | [**GenerateAiSummary**](GenerateAiSummary.md) |  | [optional] 
**search_by_titles** | [**SearchByTitles**](SearchByTitles.md) |  | [optional] 
**group_on_backend** | [**GroupOnBackend**](GroupOnBackend.md) |  | [optional] 
**multihit_weighting** | [**MultihitWeighting**](MultihitWeighting.md) |  | [optional] 
**add_bonus_from_full_content** | [**AddBonusFromFullContent**](AddBonusFromFullContent.md) |  | [optional] 
**bonus_from_full_content_threshold** | [**BonusFromFullContentThreshold**](BonusFromFullContentThreshold.md) |  | [optional] 
**bonus_from_full_content_size** | [**BonusFromFullContentSize**](BonusFromFullContentSize.md) |  | [optional] 

## Example

```python
from odin_sdk.models.project_search_request import ProjectSearchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectSearchRequest from a JSON string
project_search_request_instance = ProjectSearchRequest.from_json(json)
# print the JSON string representation of the object
print ProjectSearchRequest.to_json()

# convert the object into a dict
project_search_request_dict = project_search_request_instance.to_dict()
# create an instance of ProjectSearchRequest from a dict
project_search_request_form_dict = project_search_request.from_dict(project_search_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


