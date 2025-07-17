# BuildingBlocks

Array of json objects representing additional building blocks attachable to the agent.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from odin_sdk.models.building_blocks import BuildingBlocks

# TODO update the JSON string below
json = "{}"
# create an instance of BuildingBlocks from a JSON string
building_blocks_instance = BuildingBlocks.from_json(json)
# print the JSON string representation of the object
print BuildingBlocks.to_json()

# convert the object into a dict
building_blocks_dict = building_blocks_instance.to_dict()
# create an instance of BuildingBlocks from a dict
building_blocks_form_dict = building_blocks.from_dict(building_blocks_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


