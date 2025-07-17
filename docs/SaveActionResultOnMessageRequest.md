# SaveActionResultOnMessageRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | **object** | Project ID on which the chat and message are located. | 
**chat_id** | **object** | Chat ID on which the message is located. | 
**message_id** | **object** | Message ID on which the action result is being saved. | 
**card** | [**ResponseCardModel**](ResponseCardModel.md) | The card to be saved. | [optional] 
**is_test** | **object** | Whether the endpoint is being hit in test mode or not. | [optional] 

## Example

```python
from odin_sdk.models.save_action_result_on_message_request import SaveActionResultOnMessageRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SaveActionResultOnMessageRequest from a JSON string
save_action_result_on_message_request_instance = SaveActionResultOnMessageRequest.from_json(json)
# print the JSON string representation of the object
print SaveActionResultOnMessageRequest.to_json()

# convert the object into a dict
save_action_result_on_message_request_dict = save_action_result_on_message_request_instance.to_dict()
# create an instance of SaveActionResultOnMessageRequest from a dict
save_action_result_on_message_request_form_dict = save_action_result_on_message_request.from_dict(save_action_result_on_message_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


