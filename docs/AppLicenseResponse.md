# AppLicenseResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**seats** | [**Seats**](Seats.md) |  | [optional] 
**credits** | [**Credits**](Credits.md) |  | [optional] 
**status** | [**Status2**](Status2.md) |  | [optional] 
**plan_type** | [**PlanType**](PlanType.md) |  | [optional] 
**license_key** | **object** |  | 
**user_id** | [**UserId1**](UserId1.md) |  | [optional] 
**email** | [**Email**](Email.md) |  | [optional] 
**used** | [**Used**](Used.md) |  | [optional] 

## Example

```python
from odin_sdk.models.app_license_response import AppLicenseResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AppLicenseResponse from a JSON string
app_license_response_instance = AppLicenseResponse.from_json(json)
# print the JSON string representation of the object
print AppLicenseResponse.to_json()

# convert the object into a dict
app_license_response_dict = app_license_response_instance.to_dict()
# create an instance of AppLicenseResponse from a dict
app_license_response_form_dict = app_license_response.from_dict(app_license_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


