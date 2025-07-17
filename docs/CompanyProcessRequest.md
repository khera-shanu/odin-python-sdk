# CompanyProcessRequest

Pydantic model representing the complete request for processing company filings.  Attributes:     company (CompanyData): Company information including ticker, name, and forms to process.     project_api_key (str): API key for project authentication.     project_api_secret (str): API secret for project authentication.     project_id (str): Unique identifier for the target project.     base_url (str): Base URL of the project API.     state_file (Optional[str]): Path to state file for tracking processed filings.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**company** | [**CompanyData**](CompanyData.md) |  | 
**project_api_key** | **object** | Project API Key | 
**project_api_secret** | **object** | Project API Secret | 
**project_id** | **object** | Project ID of the Project where you want to add the processed filings | 
**base_url** | **object** | URL of Project where you want to add the processed filings | 
**state_file** | [**StateFile**](StateFile.md) |  | [optional] 

## Example

```python
from odin_sdk.models.company_process_request import CompanyProcessRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CompanyProcessRequest from a JSON string
company_process_request_instance = CompanyProcessRequest.from_json(json)
# print the JSON string representation of the object
print CompanyProcessRequest.to_json()

# convert the object into a dict
company_process_request_dict = company_process_request_instance.to_dict()
# create an instance of CompanyProcessRequest from a dict
company_process_request_form_dict = company_process_request.from_dict(company_process_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


