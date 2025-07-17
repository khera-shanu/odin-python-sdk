# PublishToolRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**version_type** | **object** | Version increment type: major, minor, or patch | [optional] 
**change_log** | [**ChangeLog1**](ChangeLog1.md) |  | [optional] 

## Example

```python
from odin_sdk.models.publish_tool_request import PublishToolRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PublishToolRequest from a JSON string
publish_tool_request_instance = PublishToolRequest.from_json(json)
# print the JSON string representation of the object
print PublishToolRequest.to_json()

# convert the object into a dict
publish_tool_request_dict = publish_tool_request_instance.to_dict()
# create an instance of PublishToolRequest from a dict
publish_tool_request_form_dict = publish_tool_request.from_dict(publish_tool_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


