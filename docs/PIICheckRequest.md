# PIICheckRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | [**ProjectId5**](ProjectId5.md) |  | [optional] 
**content_keys** | [**ContentKeys1**](ContentKeys1.md) |  | [optional] 
**content** | [**Content1**](Content1.md) |  | [optional] 
**scrub_pii** | [**ScrubPii**](ScrubPii.md) |  | [optional] 

## Example

```python
from odin_sdk.models.pii_check_request import PIICheckRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PIICheckRequest from a JSON string
pii_check_request_instance = PIICheckRequest.from_json(json)
# print the JSON string representation of the object
print PIICheckRequest.to_json()

# convert the object into a dict
pii_check_request_dict = pii_check_request_instance.to_dict()
# create an instance of PIICheckRequest from a dict
pii_check_request_form_dict = pii_check_request.from_dict(pii_check_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


