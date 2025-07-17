# DbEvalQnAPair


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **object** |  | 
**question** | **object** |  | 
**answer** | **object** |  | 
**relevant_chunks** | **object** |  | 
**chunk_ids** | **object** |  | 
**citation_correctness** | [**CitationCorrectness**](CitationCorrectness.md) |  | [optional] 
**citation_redundancy** | [**CitationRedundancy**](CitationRedundancy.md) |  | [optional] 
**retrieval_correctness** | [**RetrievalCorrectness**](RetrievalCorrectness.md) |  | [optional] 
**retrieval_precision** | [**RetrievalPrecision**](RetrievalPrecision.md) |  | [optional] 
**document_keys** | [**DocumentKeys1**](DocumentKeys1.md) |  | [optional] 
**created_at** | **object** |  | 
**updated_at** | **object** |  | 
**project_id** | [**ProjectId**](ProjectId.md) |  | [optional] 

## Example

```python
from odin_sdk.models.db_eval_qn_a_pair import DbEvalQnAPair

# TODO update the JSON string below
json = "{}"
# create an instance of DbEvalQnAPair from a JSON string
db_eval_qn_a_pair_instance = DbEvalQnAPair.from_json(json)
# print the JSON string representation of the object
print DbEvalQnAPair.to_json()

# convert the object into a dict
db_eval_qn_a_pair_dict = db_eval_qn_a_pair_instance.to_dict()
# create an instance of DbEvalQnAPair from a dict
db_eval_qn_a_pair_form_dict = db_eval_qn_a_pair.from_dict(db_eval_qn_a_pair_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


