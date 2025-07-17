# GetChatAuditHistoryResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | **object** |  | 
**chat_id** | **object** |  | 
**messages** | **object** |  | 

## Example

```python
from odin_sdk.models.get_chat_audit_history_response import GetChatAuditHistoryResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetChatAuditHistoryResponse from a JSON string
get_chat_audit_history_response_instance = GetChatAuditHistoryResponse.from_json(json)
# print the JSON string representation of the object
print GetChatAuditHistoryResponse.to_json()

# convert the object into a dict
get_chat_audit_history_response_dict = get_chat_audit_history_response_instance.to_dict()
# create an instance of GetChatAuditHistoryResponse from a dict
get_chat_audit_history_response_form_dict = get_chat_audit_history_response.from_dict(get_chat_audit_history_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


