# AnalyticsRules


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**view** | **object** | view permission for analytics | [optional] 
**edit** | **object** | edit permission for analytics | [optional] 

## Example

```python
from odin_sdk.models.analytics_rules import AnalyticsRules

# TODO update the JSON string below
json = "{}"
# create an instance of AnalyticsRules from a JSON string
analytics_rules_instance = AnalyticsRules.from_json(json)
# print the JSON string representation of the object
print AnalyticsRules.to_json()

# convert the object into a dict
analytics_rules_dict = analytics_rules_instance.to_dict()
# create an instance of AnalyticsRules from a dict
analytics_rules_form_dict = analytics_rules.from_dict(analytics_rules_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


