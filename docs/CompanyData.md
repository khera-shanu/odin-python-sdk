# CompanyData

Pydantic model representing company information for processing SEC filings.  Attributes:     ticker (str): The stock ticker symbol of the company.     name (str): The full legal name of the company.     forms (List[str]): List of SEC form types to process (e.g., [\"10-K\", \"10-Q\"]).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ticker** | **object** | Company Ticker | 
**name** | **object** | Company Name | 
**forms** | **object** | Forms to process | 

## Example

```python
from odin_sdk.models.company_data import CompanyData

# TODO update the JSON string below
json = "{}"
# create an instance of CompanyData from a JSON string
company_data_instance = CompanyData.from_json(json)
# print the JSON string representation of the object
print CompanyData.to_json()

# convert the object into a dict
company_data_dict = company_data_instance.to_dict()
# create an instance of CompanyData from a dict
company_data_form_dict = company_data.from_dict(company_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


