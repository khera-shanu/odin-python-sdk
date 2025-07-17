# SendMessageGroupResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **object** |  | 
**chat_id** | **object** |  | 

## Example

```python
from odin_sdk.models.send_message_group_response import SendMessageGroupResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SendMessageGroupResponse from a JSON string
send_message_group_response_instance = SendMessageGroupResponse.from_json(json)
# print the JSON string representation of the object
print SendMessageGroupResponse.to_json()

# convert the object into a dict
send_message_group_response_dict = send_message_group_response_instance.to_dict()
# create an instance of SendMessageGroupResponse from a dict
send_message_group_response_form_dict = send_message_group_response.from_dict(send_message_group_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


