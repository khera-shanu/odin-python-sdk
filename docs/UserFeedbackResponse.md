# UserFeedbackResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **object** |  | 
**chat_id** | **object** |  | 

## Example

```python
from odin_sdk.models.user_feedback_response import UserFeedbackResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UserFeedbackResponse from a JSON string
user_feedback_response_instance = UserFeedbackResponse.from_json(json)
# print the JSON string representation of the object
print UserFeedbackResponse.to_json()

# convert the object into a dict
user_feedback_response_dict = user_feedback_response_instance.to_dict()
# create an instance of UserFeedbackResponse from a dict
user_feedback_response_form_dict = user_feedback_response.from_dict(user_feedback_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


