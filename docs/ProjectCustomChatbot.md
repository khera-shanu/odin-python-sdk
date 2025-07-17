# ProjectCustomChatbot


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**input_placeholder_text** | [**Inputplaceholdertext**](Inputplaceholdertext.md) |  | [optional] 
**display_sources** | [**Displaysources**](Displaysources.md) |  | [optional] 
**primary_color** | [**Primarycolor**](Primarycolor.md) |  | [optional] 
**font_size** | [**Fontsize**](Fontsize.md) |  | [optional] 
**toggle_icon_color** | [**Toggleiconcolor**](Toggleiconcolor.md) |  | [optional] 
**text_color** | [**Textcolor**](Textcolor.md) |  | [optional] 
**caret_bg_color** | [**Caretbgcolor**](Caretbgcolor.md) |  | [optional] 
**suggestions** | [**Suggestions**](Suggestions.md) |  | [optional] 
**chatbot_name** | [**Chatbotname**](Chatbotname.md) |  | [optional] 
**enable_multiple_chats** | [**Enablemultiplechats**](Enablemultiplechats.md) |  | [optional] 
**auto_show_welcome_message_after** | [**Autoshowwelcomemessageafter**](Autoshowwelcomemessageafter.md) |  | [optional] 
**welcome_message** | [**Welcomemessage**](Welcomemessage.md) |  | [optional] 

## Example

```python
from odin_sdk.models.project_custom_chatbot import ProjectCustomChatbot

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectCustomChatbot from a JSON string
project_custom_chatbot_instance = ProjectCustomChatbot.from_json(json)
# print the JSON string representation of the object
print ProjectCustomChatbot.to_json()

# convert the object into a dict
project_custom_chatbot_dict = project_custom_chatbot_instance.to_dict()
# create an instance of ProjectCustomChatbot from a dict
project_custom_chatbot_form_dict = project_custom_chatbot.from_dict(project_custom_chatbot_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


