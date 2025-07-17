# RulesChat


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**edit** | **object** | create permission for chat | [optional] 
**view_all** | **object** | view permission for all chats | [optional] 
**view_mine** | **object** | view permission for my chats | [optional] 

## Example

```python
from odin_sdk.models.rules_chat import RulesChat

# TODO update the JSON string below
json = "{}"
# create an instance of RulesChat from a JSON string
rules_chat_instance = RulesChat.from_json(json)
# print the JSON string representation of the object
print RulesChat.to_json()

# convert the object into a dict
rules_chat_dict = rules_chat_instance.to_dict()
# create an instance of RulesChat from a dict
rules_chat_form_dict = rules_chat.from_dict(rules_chat_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


