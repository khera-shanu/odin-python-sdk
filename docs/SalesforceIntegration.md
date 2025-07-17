# SalesforceIntegration


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uid** | **object** |  | 
**salesforce_email** | **object** |  | 
**salesforce_instance_url** | [**SalesforceInstanceUrl**](SalesforceInstanceUrl.md) |  | [optional] 

## Example

```python
from odin_sdk.models.salesforce_integration import SalesforceIntegration

# TODO update the JSON string below
json = "{}"
# create an instance of SalesforceIntegration from a JSON string
salesforce_integration_instance = SalesforceIntegration.from_json(json)
# print the JSON string representation of the object
print SalesforceIntegration.to_json()

# convert the object into a dict
salesforce_integration_dict = salesforce_integration_instance.to_dict()
# create an instance of SalesforceIntegration from a dict
salesforce_integration_form_dict = salesforce_integration.from_dict(salesforce_integration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


