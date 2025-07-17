# FetchSimilaritiesForContentKeyRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | **object** |  | 
**document_key** | **object** |  | 
**similarity_threshold** | **object** |  | [optional] 

## Example

```python
from odin_sdk.models.fetch_similarities_for_content_key_request import FetchSimilaritiesForContentKeyRequest

# TODO update the JSON string below
json = "{}"
# create an instance of FetchSimilaritiesForContentKeyRequest from a JSON string
fetch_similarities_for_content_key_request_instance = FetchSimilaritiesForContentKeyRequest.from_json(json)
# print the JSON string representation of the object
print FetchSimilaritiesForContentKeyRequest.to_json()

# convert the object into a dict
fetch_similarities_for_content_key_request_dict = fetch_similarities_for_content_key_request_instance.to_dict()
# create an instance of FetchSimilaritiesForContentKeyRequest from a dict
fetch_similarities_for_content_key_request_form_dict = fetch_similarities_for_content_key_request.from_dict(fetch_similarities_for_content_key_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


