# UpdateClassificationRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**classification_id** | **object** |  | 
**data** | [**Classification**](Classification.md) |  | 

## Example

```python
from odin_sdk.models.update_classification_request import UpdateClassificationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateClassificationRequest from a JSON string
update_classification_request_instance = UpdateClassificationRequest.from_json(json)
# print the JSON string representation of the object
print UpdateClassificationRequest.to_json()

# convert the object into a dict
update_classification_request_dict = update_classification_request_instance.to_dict()
# create an instance of UpdateClassificationRequest from a dict
update_classification_request_form_dict = update_classification_request.from_dict(update_classification_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


