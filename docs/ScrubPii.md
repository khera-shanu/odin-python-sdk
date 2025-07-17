# ScrubPii

Whether to scrub PII from the documents.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from odin_sdk.models.scrub_pii import ScrubPii

# TODO update the JSON string below
json = "{}"
# create an instance of ScrubPii from a JSON string
scrub_pii_instance = ScrubPii.from_json(json)
# print the JSON string representation of the object
print ScrubPii.to_json()

# convert the object into a dict
scrub_pii_dict = scrub_pii_instance.to_dict()
# create an instance of ScrubPii from a dict
scrub_pii_form_dict = scrub_pii.from_dict(scrub_pii_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


