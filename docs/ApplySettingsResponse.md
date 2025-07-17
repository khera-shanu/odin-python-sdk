# ApplySettingsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **object** |  | 
**message** | **object** |  | 
**job_id** | [**JobId**](JobId.md) |  | [optional] 
**sync_status** | **object** |  | 

## Example

```python
from odin_sdk.models.apply_settings_response import ApplySettingsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ApplySettingsResponse from a JSON string
apply_settings_response_instance = ApplySettingsResponse.from_json(json)
# print the JSON string representation of the object
print ApplySettingsResponse.to_json()

# convert the object into a dict
apply_settings_response_dict = apply_settings_response_instance.to_dict()
# create an instance of ApplySettingsResponse from a dict
apply_settings_response_form_dict = apply_settings_response.from_dict(apply_settings_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


