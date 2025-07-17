# ArtifactV3

Model for the main artifact containing multiple contents.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**current_index** | **object** |  | 
**contents** | **object** |  | 

## Example

```python
from odin_sdk.models.artifact_v3 import ArtifactV3

# TODO update the JSON string below
json = "{}"
# create an instance of ArtifactV3 from a JSON string
artifact_v3_instance = ArtifactV3.from_json(json)
# print the JSON string representation of the object
print ArtifactV3.to_json()

# convert the object into a dict
artifact_v3_dict = artifact_v3_instance.to_dict()
# create an instance of ArtifactV3 from a dict
artifact_v3_form_dict = artifact_v3.from_dict(artifact_v3_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


