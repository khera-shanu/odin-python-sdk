# RulesSettings


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**view** | **object** | view permission for settings | [optional] 
**edit** | **object** | edit permission for settings | [optional] 

## Example

```python
from odin_sdk.models.rules_settings import RulesSettings

# TODO update the JSON string below
json = "{}"
# create an instance of RulesSettings from a JSON string
rules_settings_instance = RulesSettings.from_json(json)
# print the JSON string representation of the object
print RulesSettings.to_json()

# convert the object into a dict
rules_settings_dict = rules_settings_instance.to_dict()
# create an instance of RulesSettings from a dict
rules_settings_form_dict = rules_settings.from_dict(rules_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


