# CreateQAPairRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**question** | **object** |  | 
**answer** | **object** |  | 
**context** | [**Context**](Context.md) |  | [optional] 
**status** | [**Status3**](Status3.md) |  | [optional] 
**doc_key** | [**DocKey**](DocKey.md) |  | [optional] 
**document_id** | [**DocumentId**](DocumentId.md) |  | [optional] 
**type** | [**Type1**](Type1.md) |  | [optional] 

## Example

```python
from odin_sdk.models.create_qa_pair_request import CreateQAPairRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateQAPairRequest from a JSON string
create_qa_pair_request_instance = CreateQAPairRequest.from_json(json)
# print the JSON string representation of the object
print CreateQAPairRequest.to_json()

# convert the object into a dict
create_qa_pair_request_dict = create_qa_pair_request_instance.to_dict()
# create an instance of CreateQAPairRequest from a dict
create_qa_pair_request_form_dict = create_qa_pair_request.from_dict(create_qa_pair_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


