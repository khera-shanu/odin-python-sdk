# CompareRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | **object** | The ID of the project on which to execute the action. | 
**document_1** | [**Document1**](Document1.md) |  | [optional] 
**document_2** | [**Document2**](Document2.md) |  | [optional] 
**doc_1_content** | [**Doc1Content**](Doc1Content.md) |  | [optional] 
**doc_2_content** | [**Doc2Content**](Doc2Content.md) |  | [optional] 
**ignore_instructions** | [**IgnoreInstructions**](IgnoreInstructions.md) |  | [optional] 
**credit_usage_limit** | [**CreditUsageLimit**](CreditUsageLimit.md) |  | [optional] 
**diff_ai_overide_limit** | [**DiffAiOverideLimit**](DiffAiOverideLimit.md) |  | [optional] 
**sent_from_automator** | [**SentFromAutomator1**](SentFromAutomator1.md) |  | [optional] 
**wait_till_complete** | [**WaitTillComplete**](WaitTillComplete.md) |  | [optional] 

## Example

```python
from odin_sdk.models.compare_request import CompareRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CompareRequest from a JSON string
compare_request_instance = CompareRequest.from_json(json)
# print the JSON string representation of the object
print CompareRequest.to_json()

# convert the object into a dict
compare_request_dict = compare_request_instance.to_dict()
# create an instance of CompareRequest from a dict
compare_request_form_dict = compare_request.from_dict(compare_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


