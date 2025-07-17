# PurchaseSeatsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**seats** | **object** |  | 
**operation** | **object** |  | 

## Example

```python
from odin_sdk.models.purchase_seats_request import PurchaseSeatsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PurchaseSeatsRequest from a JSON string
purchase_seats_request_instance = PurchaseSeatsRequest.from_json(json)
# print the JSON string representation of the object
print PurchaseSeatsRequest.to_json()

# convert the object into a dict
purchase_seats_request_dict = purchase_seats_request_instance.to_dict()
# create an instance of PurchaseSeatsRequest from a dict
purchase_seats_request_form_dict = purchase_seats_request.from_dict(purchase_seats_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


