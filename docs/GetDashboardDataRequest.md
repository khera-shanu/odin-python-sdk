# GetDashboardDataRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**widgets** | **object** | List of widgets to fetch data for | 
**global_filters** | [**GlobalFilters**](GlobalFilters.md) |  | [optional] 
**dashboard_period** | [**DashboardPeriod**](DashboardPeriod.md) |  | [optional] 

## Example

```python
from odin_sdk.models.get_dashboard_data_request import GetDashboardDataRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GetDashboardDataRequest from a JSON string
get_dashboard_data_request_instance = GetDashboardDataRequest.from_json(json)
# print the JSON string representation of the object
print GetDashboardDataRequest.to_json()

# convert the object into a dict
get_dashboard_data_request_dict = get_dashboard_data_request_instance.to_dict()
# create an instance of GetDashboardDataRequest from a dict
get_dashboard_data_request_form_dict = get_dashboard_data_request.from_dict(get_dashboard_data_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


