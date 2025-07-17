# TestExecuteRequest

Request model for test execution without database persistence

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**runtime** | **object** | Runtime version (e.g., &#39;python3.11&#39;, &#39;nodejs20.x&#39;) | 
**script** | **object** | Script code to execute | 
**entry_point** | **object** | Entry point function name | [optional] 
**dependencies** | **object** | List of package dependencies | [optional] 
**args** | **object** | Positional arguments | [optional] 
**kwargs** | **object** | Keyword arguments | [optional] 

## Example

```python
from odin_sdk.models.test_execute_request import TestExecuteRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TestExecuteRequest from a JSON string
test_execute_request_instance = TestExecuteRequest.from_json(json)
# print the JSON string representation of the object
print TestExecuteRequest.to_json()

# convert the object into a dict
test_execute_request_dict = test_execute_request_instance.to_dict()
# create an instance of TestExecuteRequest from a dict
test_execute_request_form_dict = test_execute_request.from_dict(test_execute_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


