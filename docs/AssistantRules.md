# AssistantRules


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**edit** | **object** | create permission for assistant | [optional] 
**view** | **object** | view permission for assistants | [optional] 

## Example

```python
from odin_sdk.models.assistant_rules import AssistantRules

# TODO update the JSON string below
json = "{}"
# create an instance of AssistantRules from a JSON string
assistant_rules_instance = AssistantRules.from_json(json)
# print the JSON string representation of the object
print AssistantRules.to_json()

# convert the object into a dict
assistant_rules_dict = assistant_rules_instance.to_dict()
# create an instance of AssistantRules from a dict
assistant_rules_form_dict = assistant_rules.from_dict(assistant_rules_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


