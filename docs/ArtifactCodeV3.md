# ArtifactCodeV3

Model for code artifact content.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**index** | **object** |  | 
**type** | **object** |  | 
**title** | **object** |  | 
**language** | **object** |  | 
**code** | **object** |  | 

## Example

```python
from odin_sdk.models.artifact_code_v3 import ArtifactCodeV3

# TODO update the JSON string below
json = "{}"
# create an instance of ArtifactCodeV3 from a JSON string
artifact_code_v3_instance = ArtifactCodeV3.from_json(json)
# print the JSON string representation of the object
print ArtifactCodeV3.to_json()

# convert the object into a dict
artifact_code_v3_dict = artifact_code_v3_instance.to_dict()
# create an instance of ArtifactCodeV3 from a dict
artifact_code_v3_form_dict = artifact_code_v3.from_dict(artifact_code_v3_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


