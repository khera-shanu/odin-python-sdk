# BringOwnRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | **object** |  | 
**url** | [**Url**](Url.md) |  | [optional] 
**api_key** | **object** |  | 

## Example

```python
from odin_sdk.models.bring_own_request import BringOwnRequest

# TODO update the JSON string below
json = "{}"
# create an instance of BringOwnRequest from a JSON string
bring_own_request_instance = BringOwnRequest.from_json(json)
# print the JSON string representation of the object
print BringOwnRequest.to_json()

# convert the object into a dict
bring_own_request_dict = bring_own_request_instance.to_dict()
# create an instance of BringOwnRequest from a dict
bring_own_request_form_dict = bring_own_request.from_dict(bring_own_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


