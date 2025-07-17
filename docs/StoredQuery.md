# StoredQuery


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **object** |  | 
**query_text** | **object** |  | 
**doc_ids** | **object** |  | 

## Example

```python
from odin_sdk.models.stored_query import StoredQuery

# TODO update the JSON string below
json = "{}"
# create an instance of StoredQuery from a JSON string
stored_query_instance = StoredQuery.from_json(json)
# print the JSON string representation of the object
print StoredQuery.to_json()

# convert the object into a dict
stored_query_dict = stored_query_instance.to_dict()
# create an instance of StoredQuery from a dict
stored_query_form_dict = stored_query.from_dict(stored_query_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


