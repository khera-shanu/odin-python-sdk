# Rules


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**chat** | [**RulesChat**](RulesChat.md) |  | [optional] 
**assistant** | [**RulesAssistant**](RulesAssistant.md) |  | [optional] 
**document** | [**RulesDocument**](RulesDocument.md) |  | [optional] 
**agents** | [**RulesAgents**](RulesAgents.md) |  | [optional] 
**settings** | [**RulesSettings**](RulesSettings.md) |  | [optional] 
**add_members** | [**RulesAddMembers**](RulesAddMembers.md) |  | [optional] 
**kb** | [**RulesKb**](RulesKb.md) |  | [optional] 
**flows** | [**RulesFlows**](RulesFlows.md) |  | [optional] 
**analytics** | [**RulesAnalytics**](RulesAnalytics.md) |  | [optional] 
**actions** | [**RulesActions**](RulesActions.md) |  | [optional] 
**roles** | [**RulesRoles**](RulesRoles.md) |  | [optional] 

## Example

```python
from odin_sdk.models.rules import Rules

# TODO update the JSON string below
json = "{}"
# create an instance of Rules from a JSON string
rules_instance = Rules.from_json(json)
# print the JSON string representation of the object
print Rules.to_json()

# convert the object into a dict
rules_dict = rules_instance.to_dict()
# create an instance of Rules from a dict
rules_form_dict = rules.from_dict(rules_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


