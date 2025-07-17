# Pii

The PII extracted from the content of the document.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from odin_sdk.models.pii import Pii

# TODO update the JSON string below
json = "{}"
# create an instance of Pii from a JSON string
pii_instance = Pii.from_json(json)
# print the JSON string representation of the object
print Pii.to_json()

# convert the object into a dict
pii_dict = pii_instance.to_dict()
# create an instance of Pii from a dict
pii_form_dict = pii.from_dict(pii_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


