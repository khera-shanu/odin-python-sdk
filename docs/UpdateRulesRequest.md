# UpdateRulesRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**chat** | [**UpdateRulesRequestChat**](UpdateRulesRequestChat.md) |  | [optional] 
**assistant** | [**UpdateRulesRequestAssistant**](UpdateRulesRequestAssistant.md) |  | [optional] 
**document** | [**UpdateRulesRequestDocument**](UpdateRulesRequestDocument.md) |  | [optional] 
**agents** | [**UpdateRulesRequestAgents**](UpdateRulesRequestAgents.md) |  | [optional] 
**settings** | [**UpdateRulesRequestSettings**](UpdateRulesRequestSettings.md) |  | [optional] 
**add_members** | [**UpdateRulesRequestAddMembers**](UpdateRulesRequestAddMembers.md) |  | [optional] 
**kb** | [**UpdateRulesRequestKb**](UpdateRulesRequestKb.md) |  | [optional] 
**flows** | [**UpdateRulesRequestFlows**](UpdateRulesRequestFlows.md) |  | [optional] 
**analytics** | [**UpdateRulesRequestAnalytics**](UpdateRulesRequestAnalytics.md) |  | [optional] 
**actions** | [**UpdateRulesRequestActions**](UpdateRulesRequestActions.md) |  | [optional] 
**roles** | [**UpdateRulesRequestRoles**](UpdateRulesRequestRoles.md) |  | [optional] 

## Example

```python
from odin_sdk.models.update_rules_request import UpdateRulesRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateRulesRequest from a JSON string
update_rules_request_instance = UpdateRulesRequest.from_json(json)
# print the JSON string representation of the object
print UpdateRulesRequest.to_json()

# convert the object into a dict
update_rules_request_dict = update_rules_request_instance.to_dict()
# create an instance of UpdateRulesRequest from a dict
update_rules_request_form_dict = update_rules_request.from_dict(update_rules_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


