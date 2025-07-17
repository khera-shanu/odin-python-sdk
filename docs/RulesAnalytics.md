# RulesAnalytics


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**view** | **object** | view permission for analytics | [optional] 
**edit** | **object** | edit permission for analytics | [optional] 

## Example

```python
from odin_sdk.models.rules_analytics import RulesAnalytics

# TODO update the JSON string below
json = "{}"
# create an instance of RulesAnalytics from a JSON string
rules_analytics_instance = RulesAnalytics.from_json(json)
# print the JSON string representation of the object
print RulesAnalytics.to_json()

# convert the object into a dict
rules_analytics_dict = rules_analytics_instance.to_dict()
# create an instance of RulesAnalytics from a dict
rules_analytics_form_dict = rules_analytics.from_dict(rules_analytics_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


