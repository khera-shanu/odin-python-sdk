# StatusChange


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sub_code** | [**SubCode**](SubCode.md) |  | [optional] 
**created_at** | **object** |  | 
**code** | **object** |  | 
**message** | [**Message1**](Message1.md) |  | [optional] 

## Example

```python
from odin_sdk.models.status_change import StatusChange

# TODO update the JSON string below
json = "{}"
# create an instance of StatusChange from a JSON string
status_change_instance = StatusChange.from_json(json)
# print the JSON string representation of the object
print StatusChange.to_json()

# convert the object into a dict
status_change_dict = status_change_instance.to_dict()
# create an instance of StatusChange from a dict
status_change_form_dict = status_change.from_dict(status_change_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


