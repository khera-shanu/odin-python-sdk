# CreateTestGroupRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | **object** |  | 
**name** | **object** |  | 
**agent_id** | [**AgentId**](AgentId.md) |  | [optional] 
**agent_name** | [**AgentName**](AgentName.md) |  | [optional] 

## Example

```python
from odin_sdk.models.create_test_group_request import CreateTestGroupRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateTestGroupRequest from a JSON string
create_test_group_request_instance = CreateTestGroupRequest.from_json(json)
# print the JSON string representation of the object
print CreateTestGroupRequest.to_json()

# convert the object into a dict
create_test_group_request_dict = create_test_group_request_instance.to_dict()
# create an instance of CreateTestGroupRequest from a dict
create_test_group_request_form_dict = create_test_group_request.from_dict(create_test_group_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


