# AuditLog


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **object** |  | 
**secret_id** | **object** |  | 
**user_id** | **object** |  | 
**user** | [**AuditLogUser**](AuditLogUser.md) |  | 
**action** | **object** |  | 
**details** | **object** |  | 
**created_at** | **object** |  | 

## Example

```python
from odin_sdk.models.audit_log import AuditLog

# TODO update the JSON string below
json = "{}"
# create an instance of AuditLog from a JSON string
audit_log_instance = AuditLog.from_json(json)
# print the JSON string representation of the object
print AuditLog.to_json()

# convert the object into a dict
audit_log_dict = audit_log_instance.to_dict()
# create an instance of AuditLog from a dict
audit_log_form_dict = audit_log.from_dict(audit_log_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


