# TestApiToolResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **object** | Whether the API request was successful | 
**message** | **object** | A message describing the result | 
**flow_run_id** | [**FlowRunId1**](FlowRunId1.md) |  | [optional] 
**response** | [**Response**](Response.md) |  | [optional] 
**chat_id** | [**ChatId5**](ChatId5.md) |  | [optional] 
**message_id** | [**MessageId5**](MessageId5.md) |  | [optional] 

## Example

```python
from odin_sdk.models.test_api_tool_response import TestApiToolResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TestApiToolResponse from a JSON string
test_api_tool_response_instance = TestApiToolResponse.from_json(json)
# print the JSON string representation of the object
print TestApiToolResponse.to_json()

# convert the object into a dict
test_api_tool_response_dict = test_api_tool_response_instance.to_dict()
# create an instance of TestApiToolResponse from a dict
test_api_tool_response_form_dict = test_api_tool_response.from_dict(test_api_tool_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


