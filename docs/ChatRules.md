# ChatRules


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**edit** | **object** | create permission for chat | [optional] 
**view_all** | **object** | view permission for all chats | [optional] 
**view_mine** | **object** | view permission for my chats | [optional] 

## Example

```python
from odin_sdk.models.chat_rules import ChatRules

# TODO update the JSON string below
json = "{}"
# create an instance of ChatRules from a JSON string
chat_rules_instance = ChatRules.from_json(json)
# print the JSON string representation of the object
print ChatRules.to_json()

# convert the object into a dict
chat_rules_dict = chat_rules_instance.to_dict()
# create an instance of ChatRules from a dict
chat_rules_form_dict = chat_rules.from_dict(chat_rules_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


