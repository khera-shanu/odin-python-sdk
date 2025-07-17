# RulesKb


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**view** | **object** | view permission for kb | [optional] 
**edit** | **object** | edit permission for kb | [optional] 

## Example

```python
from odin_sdk.models.rules_kb import RulesKb

# TODO update the JSON string below
json = "{}"
# create an instance of RulesKb from a JSON string
rules_kb_instance = RulesKb.from_json(json)
# print the JSON string representation of the object
print RulesKb.to_json()

# convert the object into a dict
rules_kb_dict = rules_kb_instance.to_dict()
# create an instance of RulesKb from a dict
rules_kb_form_dict = rules_kb.from_dict(rules_kb_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


