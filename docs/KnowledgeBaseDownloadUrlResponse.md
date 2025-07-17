# KnowledgeBaseDownloadUrlResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**download_url** | **object** |  | 
**metadata_url** | [**MetadataUrl**](MetadataUrl.md) |  | [optional] 

## Example

```python
from odin_sdk.models.knowledge_base_download_url_response import KnowledgeBaseDownloadUrlResponse

# TODO update the JSON string below
json = "{}"
# create an instance of KnowledgeBaseDownloadUrlResponse from a JSON string
knowledge_base_download_url_response_instance = KnowledgeBaseDownloadUrlResponse.from_json(json)
# print the JSON string representation of the object
print KnowledgeBaseDownloadUrlResponse.to_json()

# convert the object into a dict
knowledge_base_download_url_response_dict = knowledge_base_download_url_response_instance.to_dict()
# create an instance of KnowledgeBaseDownloadUrlResponse from a dict
knowledge_base_download_url_response_form_dict = knowledge_base_download_url_response.from_dict(knowledge_base_download_url_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


