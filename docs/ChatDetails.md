# ChatDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**updated_at** | **object** |  | [optional] 
**name** | **object** |  | [optional] 
**document_keys** | [**DocumentKeys1**](DocumentKeys1.md) |  | [optional] 
**created_by** | **object** |  | [optional] 
**metadata** | [**Metadata1**](Metadata1.md) |  | [optional] 
**created_at** | **object** |  | [optional] 
**id** | **object** |  | [optional] 

## Example

```python
from odin_sdk.models.chat_details import ChatDetails

# TODO update the JSON string below
json = "{}"
# create an instance of ChatDetails from a JSON string
chat_details_instance = ChatDetails.from_json(json)
# print the JSON string representation of the object
print ChatDetails.to_json()

# convert the object into a dict
chat_details_dict = chat_details_instance.to_dict()
# create an instance of ChatDetails from a dict
chat_details_form_dict = chat_details.from_dict(chat_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


