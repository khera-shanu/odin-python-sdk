# ProjectResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **object** |  | 
**name** | [**Name**](Name.md) |  | 
**owner** | [**Owner**](Owner.md) |  | 
**members** | [**Members1**](Members1.md) |  | 
**created_at** | [**CreatedAt**](CreatedAt.md) |  | 
**team_id** | [**TeamId**](TeamId.md) |  | 
**credits_used** | [**CreditsUsed1**](CreditsUsed1.md) |  | [optional] 
**agents_created** | [**AgentsCreated**](AgentsCreated.md) |  | [optional] 

## Example

```python
from odin_sdk.models.project_response import ProjectResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectResponse from a JSON string
project_response_instance = ProjectResponse.from_json(json)
# print the JSON string representation of the object
print ProjectResponse.to_json()

# convert the object into a dict
project_response_dict = project_response_instance.to_dict()
# create an instance of ProjectResponse from a dict
project_response_form_dict = project_response.from_dict(project_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


