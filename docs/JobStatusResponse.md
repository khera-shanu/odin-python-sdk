# JobStatusResponse

Response model for job status check

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**job_id** | **object** | Job identifier | 
**status** | **object** | Current job status | 
**result** | [**Result1**](Result1.md) |  | [optional] 
**error** | [**Error1**](Error1.md) |  | [optional] 
**progress** | [**Progress**](Progress.md) |  | [optional] 
**created_at** | [**CreatedAt2**](CreatedAt2.md) |  | [optional] 
**updated_at** | [**UpdatedAt2**](UpdatedAt2.md) |  | [optional] 
**completed_at** | [**CompletedAt2**](CompletedAt2.md) |  | [optional] 

## Example

```python
from odin_sdk.models.job_status_response import JobStatusResponse

# TODO update the JSON string below
json = "{}"
# create an instance of JobStatusResponse from a JSON string
job_status_response_instance = JobStatusResponse.from_json(json)
# print the JSON string representation of the object
print JobStatusResponse.to_json()

# convert the object into a dict
job_status_response_dict = job_status_response_instance.to_dict()
# create an instance of JobStatusResponse from a dict
job_status_response_form_dict = job_status_response.from_dict(job_status_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


