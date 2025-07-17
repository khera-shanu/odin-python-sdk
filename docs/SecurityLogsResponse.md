# SecurityLogsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**actions** | **object** |  | 

## Example

```python
from odin_sdk.models.security_logs_response import SecurityLogsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SecurityLogsResponse from a JSON string
security_logs_response_instance = SecurityLogsResponse.from_json(json)
# print the JSON string representation of the object
print SecurityLogsResponse.to_json()

# convert the object into a dict
security_logs_response_dict = security_logs_response_instance.to_dict()
# create an instance of SecurityLogsResponse from a dict
security_logs_response_form_dict = security_logs_response.from_dict(security_logs_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


