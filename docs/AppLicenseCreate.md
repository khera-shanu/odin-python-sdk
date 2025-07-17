# AppLicenseCreate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**seats** | **object** |  | 
**credits** | **object** |  | 
**status** | [**Status2**](Status2.md) |  | [optional] 
**plan_type** | [**PlanType**](PlanType.md) |  | [optional] 

## Example

```python
from odin_sdk.models.app_license_create import AppLicenseCreate

# TODO update the JSON string below
json = "{}"
# create an instance of AppLicenseCreate from a JSON string
app_license_create_instance = AppLicenseCreate.from_json(json)
# print the JSON string representation of the object
print AppLicenseCreate.to_json()

# convert the object into a dict
app_license_create_dict = app_license_create_instance.to_dict()
# create an instance of AppLicenseCreate from a dict
app_license_create_form_dict = app_license_create.from_dict(app_license_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


