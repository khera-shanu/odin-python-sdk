# GetChatbotResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **object** |  | 
**custom_chatbot** | **object** |  | [optional] 

## Example

```python
from odin_sdk.models.get_chatbot_response import GetChatbotResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetChatbotResponse from a JSON string
get_chatbot_response_instance = GetChatbotResponse.from_json(json)
# print the JSON string representation of the object
print GetChatbotResponse.to_json()

# convert the object into a dict
get_chatbot_response_dict = get_chatbot_response_instance.to_dict()
# create an instance of GetChatbotResponse from a dict
get_chatbot_response_form_dict = get_chatbot_response.from_dict(get_chatbot_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


