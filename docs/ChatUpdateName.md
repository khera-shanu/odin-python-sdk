# ChatUpdateName


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | **object** |  | 
**chat_id** | **object** |  | 
**title** | **object** |  | 

## Example

```python
from odin_sdk.models.chat_update_name import ChatUpdateName

# TODO update the JSON string below
json = "{}"
# create an instance of ChatUpdateName from a JSON string
chat_update_name_instance = ChatUpdateName.from_json(json)
# print the JSON string representation of the object
print ChatUpdateName.to_json()

# convert the object into a dict
chat_update_name_dict = chat_update_name_instance.to_dict()
# create an instance of ChatUpdateName from a dict
chat_update_name_form_dict = chat_update_name.from_dict(chat_update_name_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


