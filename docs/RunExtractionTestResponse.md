# RunExtractionTestResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **object** |  | 
**results** | [**ExtractionResults**](ExtractionResults.md) |  | 
**result_type** | [**ResultType**](ResultType.md) |  | [optional] 
**should_provide_validation_score** | **object** |  | [optional] 

## Example

```python
from odin_sdk.models.run_extraction_test_response import RunExtractionTestResponse

# TODO update the JSON string below
json = "{}"
# create an instance of RunExtractionTestResponse from a JSON string
run_extraction_test_response_instance = RunExtractionTestResponse.from_json(json)
# print the JSON string representation of the object
print RunExtractionTestResponse.to_json()

# convert the object into a dict
run_extraction_test_response_dict = run_extraction_test_response_instance.to_dict()
# create an instance of RunExtractionTestResponse from a dict
run_extraction_test_response_form_dict = run_extraction_test_response.from_dict(run_extraction_test_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


