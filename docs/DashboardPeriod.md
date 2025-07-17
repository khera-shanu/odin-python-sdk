# DashboardPeriod

Dashboard-level period filter: 1h, 24h, 7d, 30d, 90d, 6m, 1y, ytd, all

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from odin_sdk.models.dashboard_period import DashboardPeriod

# TODO update the JSON string below
json = "{}"
# create an instance of DashboardPeriod from a JSON string
dashboard_period_instance = DashboardPeriod.from_json(json)
# print the JSON string representation of the object
print DashboardPeriod.to_json()

# convert the object into a dict
dashboard_period_dict = dashboard_period_instance.to_dict()
# create an instance of DashboardPeriod from a dict
dashboard_period_form_dict = dashboard_period.from_dict(dashboard_period_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


