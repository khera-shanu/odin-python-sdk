# RulesAssistant


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**edit** | **object** | create permission for assistant | [optional] 
**view** | **object** | view permission for assistants | [optional] 

## Example

```python
from odin_sdk.models.rules_assistant import RulesAssistant

# TODO update the JSON string below
json = "{}"
# create an instance of RulesAssistant from a JSON string
rules_assistant_instance = RulesAssistant.from_json(json)
# print the JSON string representation of the object
print RulesAssistant.to_json()

# convert the object into a dict
rules_assistant_dict = rules_assistant_instance.to_dict()
# create an instance of RulesAssistant from a dict
rules_assistant_form_dict = rules_assistant.from_dict(rules_assistant_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


