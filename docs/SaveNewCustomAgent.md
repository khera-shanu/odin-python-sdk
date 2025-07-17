# SaveNewCustomAgent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | **object** | ID of the project in which to create the agent. | 
**agent_name** | **object** | Custom name of the agent. | 
**personality** | **object** | Personality definition of the agent. | [optional] 
**building_blocks** | [**BuildingBlocks1**](BuildingBlocks1.md) |  | [optional] 
**temperature** | [**Temperature1**](Temperature1.md) |  | [optional] 

## Example

```python
from odin_sdk.models.save_new_custom_agent import SaveNewCustomAgent

# TODO update the JSON string below
json = "{}"
# create an instance of SaveNewCustomAgent from a JSON string
save_new_custom_agent_instance = SaveNewCustomAgent.from_json(json)
# print the JSON string representation of the object
print SaveNewCustomAgent.to_json()

# convert the object into a dict
save_new_custom_agent_dict = save_new_custom_agent_instance.to_dict()
# create an instance of SaveNewCustomAgent from a dict
save_new_custom_agent_form_dict = save_new_custom_agent.from_dict(save_new_custom_agent_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


