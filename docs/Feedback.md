# Feedback


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user** | [**User**](User.md) |  | [optional] 
**user_id** | [**UserId1**](UserId1.md) |  | [optional] 
**created_at** | [**CreatedAt**](CreatedAt.md) |  | [optional] 
**feedback_type** | **object** |  | 
**details** | **object** |  | 

## Example

```python
from odin_sdk.models.feedback import Feedback

# TODO update the JSON string below
json = "{}"
# create an instance of Feedback from a JSON string
feedback_instance = Feedback.from_json(json)
# print the JSON string representation of the object
print Feedback.to_json()

# convert the object into a dict
feedback_dict = feedback_instance.to_dict()
# create an instance of Feedback from a dict
feedback_form_dict = feedback.from_dict(feedback_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


