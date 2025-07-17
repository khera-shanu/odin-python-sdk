# ProcessCompanyResponse

Pydantic model representing the response from processing company filings.  Attributes:     status (str): Processing status ('success' or 'error').     message (str): Description of the processing result.     filings_processed (int): Number of filings processed.     filing_data (List[FilingData]): Detailed information about processed filings.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **object** |  | 
**message** | **object** |  | 
**filings_processed** | **object** |  | 
**filing_data** | **object** |  | 

## Example

```python
from odin_sdk.models.process_company_response import ProcessCompanyResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ProcessCompanyResponse from a JSON string
process_company_response_instance = ProcessCompanyResponse.from_json(json)
# print the JSON string representation of the object
print ProcessCompanyResponse.to_json()

# convert the object into a dict
process_company_response_dict = process_company_response_instance.to_dict()
# create an instance of ProcessCompanyResponse from a dict
process_company_response_form_dict = process_company_response.from_dict(process_company_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


