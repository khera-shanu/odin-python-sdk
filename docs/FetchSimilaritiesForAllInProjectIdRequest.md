# FetchSimilaritiesForAllInProjectIdRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | **object** |  | 
**similarity_threshold** | **object** |  | [optional] 

## Example

```python
from odin_sdk.models.fetch_similarities_for_all_in_project_id_request import FetchSimilaritiesForAllInProjectIdRequest

# TODO update the JSON string below
json = "{}"
# create an instance of FetchSimilaritiesForAllInProjectIdRequest from a JSON string
fetch_similarities_for_all_in_project_id_request_instance = FetchSimilaritiesForAllInProjectIdRequest.from_json(json)
# print the JSON string representation of the object
print FetchSimilaritiesForAllInProjectIdRequest.to_json()

# convert the object into a dict
fetch_similarities_for_all_in_project_id_request_dict = fetch_similarities_for_all_in_project_id_request_instance.to_dict()
# create an instance of FetchSimilaritiesForAllInProjectIdRequest from a dict
fetch_similarities_for_all_in_project_id_request_form_dict = fetch_similarities_for_all_in_project_id_request.from_dict(fetch_similarities_for_all_in_project_id_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


