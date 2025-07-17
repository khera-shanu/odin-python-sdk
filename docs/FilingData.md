# FilingData

Pydantic model representing processed filing information.  Attributes:     ticker (str): Company ticker symbol.     form (str): SEC form type.     date (int): Unix timestamp of the filing date.     url (str): URL to access the filing.     fiscal_year (Optional[int]): Fiscal year of the filing.     fiscal_quarter (Optional[str]): Fiscal quarter (e.g., 'Q4').     added_to_kb_log (Optional[str]): Log information about KB addition.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ticker** | **object** |  | 
**form** | **object** |  | 
**var_date** | **object** |  | 
**url** | **object** |  | 
**fiscal_year** | [**FiscalYear**](FiscalYear.md) |  | [optional] 
**fiscal_quarter** | [**FiscalQuarter**](FiscalQuarter.md) |  | [optional] 
**added_to_kb_log** | [**AddedToKbLog**](AddedToKbLog.md) |  | [optional] 

## Example

```python
from odin_sdk.models.filing_data import FilingData

# TODO update the JSON string below
json = "{}"
# create an instance of FilingData from a JSON string
filing_data_instance = FilingData.from_json(json)
# print the JSON string representation of the object
print FilingData.to_json()

# convert the object into a dict
filing_data_dict = filing_data_instance.to_dict()
# create an instance of FilingData from a dict
filing_data_form_dict = filing_data.from_dict(filing_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


