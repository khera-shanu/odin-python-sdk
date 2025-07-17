# PageExtractionResults


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**page_number** | **object** |  | 
**extraction** | **object** |  | 
**extraction_time_ms** | [**ExtractionTimeMs**](ExtractionTimeMs.md) |  | [optional] 
**extraction_with_comparison** | [**ExtractionWithComparison**](ExtractionWithComparison.md) |  | [optional] 
**extraction_with_confidence_from_llm** | [**ExtractionWithConfidenceFromLlm**](ExtractionWithConfidenceFromLlm.md) |  | [optional] 
**validation_error** | [**ValidationError**](ValidationError.md) |  | [optional] 

## Example

```python
from odin_sdk.models.page_extraction_results import PageExtractionResults

# TODO update the JSON string below
json = "{}"
# create an instance of PageExtractionResults from a JSON string
page_extraction_results_instance = PageExtractionResults.from_json(json)
# print the JSON string representation of the object
print PageExtractionResults.to_json()

# convert the object into a dict
page_extraction_results_dict = page_extraction_results_instance.to_dict()
# create an instance of PageExtractionResults from a dict
page_extraction_results_form_dict = page_extraction_results.from_dict(page_extraction_results_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


