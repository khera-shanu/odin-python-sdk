# Messages


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from odin_sdk.models.messages import Messages

# TODO update the JSON string below
json = "{}"
# create an instance of Messages from a JSON string
messages_instance = Messages.from_json(json)
# print the JSON string representation of the object
print Messages.to_json()

# convert the object into a dict
messages_dict = messages_instance.to_dict()
# create an instance of Messages from a dict
messages_form_dict = messages.from_dict(messages_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


