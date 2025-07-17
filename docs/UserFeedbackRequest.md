# UserFeedbackRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_feedback** | [**UserFeedback**](UserFeedback.md) |  | [optional] 
**message_id** | **object** |  | 
**project_id** | **object** |  | 
**chat_id** | **object** |  | 
**additional_feedback** | [**AdditionalFeedback**](AdditionalFeedback.md) |  | [optional] 
**is_correct_answer_option** | [**IsCorrectAnswerOption**](IsCorrectAnswerOption.md) |  | [optional] 
**notes** | [**Notes**](Notes.md) |  | [optional] 
**unit_test_existing_group_id** | [**UnitTestExistingGroupId**](UnitTestExistingGroupId.md) |  | [optional] 
**new_unit_test_group_name** | [**NewUnitTestGroupName**](NewUnitTestGroupName.md) |  | [optional] 
**question** | [**Question**](Question.md) |  | [optional] 
**expected_answer** | [**ExpectedAnswer**](ExpectedAnswer.md) |  | [optional] 
**is_incorrect_answer_option** | [**IsIncorrectAnswerOption**](IsIncorrectAnswerOption.md) |  | [optional] 
**suggested_better_response** | [**SuggestedBetterResponse**](SuggestedBetterResponse.md) |  | [optional] 
**is_incorrect_source_url_option** | [**IsIncorrectSourceUrlOption**](IsIncorrectSourceUrlOption.md) |  | [optional] 
**correct_source_url** | [**CorrectSourceUrl**](CorrectSourceUrl.md) |  | [optional] 

## Example

```python
from odin_sdk.models.user_feedback_request import UserFeedbackRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UserFeedbackRequest from a JSON string
user_feedback_request_instance = UserFeedbackRequest.from_json(json)
# print the JSON string representation of the object
print UserFeedbackRequest.to_json()

# convert the object into a dict
user_feedback_request_dict = user_feedback_request_instance.to_dict()
# create an instance of UserFeedbackRequest from a dict
user_feedback_request_form_dict = user_feedback_request.from_dict(user_feedback_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


