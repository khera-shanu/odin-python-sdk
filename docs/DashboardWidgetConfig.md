# DashboardWidgetConfig


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**column** | [**Column**](Column.md) |  | [optional] 
**chart_type** | [**ChartType**](ChartType.md) |  | [optional] 
**group_by** | [**GroupBy**](GroupBy.md) |  | [optional] 
**group_by_columns** | [**GroupByColumns**](GroupByColumns.md) |  | [optional] 
**aggregation** | [**Aggregation**](Aggregation.md) |  | [optional] 
**series** | [**Series**](Series.md) |  | [optional] 
**text_content** | [**TextContent**](TextContent.md) |  | [optional] 
**filters** | [**Filters1**](Filters1.md) |  | [optional] 
**operation** | [**Operation**](Operation.md) |  | [optional] 
**count_type** | [**CountType1**](CountType1.md) |  | [optional] 
**condition** | [**Condition**](Condition.md) |  | [optional] 
**math_enabled** | [**MathEnabled**](MathEnabled.md) |  | [optional] 
**math_operation** | [**MathOperation**](MathOperation.md) |  | [optional] 
**second_value_source** | [**SecondValueSource**](SecondValueSource.md) |  | [optional] 
**second_value_fixed** | [**SecondValueFixed**](SecondValueFixed.md) |  | [optional] 
**second_value_column** | [**SecondValueColumn**](SecondValueColumn.md) |  | [optional] 
**second_value_operation** | [**SecondValueOperation**](SecondValueOperation.md) |  | [optional] 
**second_value_widget_id** | [**SecondValueWidgetId**](SecondValueWidgetId.md) |  | [optional] 
**second_filters** | [**SecondFilters**](SecondFilters.md) |  | [optional] 
**data_source** | [**DataSource**](DataSource.md) |  | [optional] 
**date_grouping** | [**DateGrouping**](DateGrouping.md) |  | [optional] 
**inherit_dashboard_period** | [**InheritDashboardPeriod**](InheritDashboardPeriod.md) |  | [optional] 
**compare_last_period** | [**CompareLastPeriod**](CompareLastPeriod.md) |  | [optional] 

## Example

```python
from odin_sdk.models.dashboard_widget_config import DashboardWidgetConfig

# TODO update the JSON string below
json = "{}"
# create an instance of DashboardWidgetConfig from a JSON string
dashboard_widget_config_instance = DashboardWidgetConfig.from_json(json)
# print the JSON string representation of the object
print DashboardWidgetConfig.to_json()

# convert the object into a dict
dashboard_widget_config_dict = dashboard_widget_config_instance.to_dict()
# create an instance of DashboardWidgetConfig from a dict
dashboard_widget_config_form_dict = dashboard_widget_config.from_dict(dashboard_widget_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


