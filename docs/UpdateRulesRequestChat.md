# UpdateRulesRequestChat


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**view_all** | [**ViewAll**](ViewAll.md) |  | [optional] 
**view_mine** | [**ViewMine**](ViewMine.md) |  | [optional] 
**edit** | [**Edit**](Edit.md) |  | [optional] 

## Example

```python
from odin_sdk.models.update_rules_request_chat import UpdateRulesRequestChat

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateRulesRequestChat from a JSON string
update_rules_request_chat_instance = UpdateRulesRequestChat.from_json(json)
# print the JSON string representation of the object
print UpdateRulesRequestChat.to_json()

# convert the object into a dict
update_rules_request_chat_dict = update_rules_request_chat_instance.to_dict()
# create an instance of UpdateRulesRequestChat from a dict
update_rules_request_chat_form_dict = update_rules_request_chat.from_dict(update_rules_request_chat_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


