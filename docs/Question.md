# Question


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from odin_sdk.models.question import Question

# TODO update the JSON string below
json = "{}"
# create an instance of Question from a JSON string
question_instance = Question.from_json(json)
# print the JSON string representation of the object
print Question.to_json()

# convert the object into a dict
question_dict = question_instance.to_dict()
# create an instance of Question from a dict
question_form_dict = question.from_dict(question_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


