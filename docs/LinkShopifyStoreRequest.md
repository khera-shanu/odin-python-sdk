# LinkShopifyStoreRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | **object** |  | 
**shop_name** | **object** |  | 
**alias** | **object** |  | 
**shop_token** | **object** |  | 

## Example

```python
from odin_sdk.models.link_shopify_store_request import LinkShopifyStoreRequest

# TODO update the JSON string below
json = "{}"
# create an instance of LinkShopifyStoreRequest from a JSON string
link_shopify_store_request_instance = LinkShopifyStoreRequest.from_json(json)
# print the JSON string representation of the object
print LinkShopifyStoreRequest.to_json()

# convert the object into a dict
link_shopify_store_request_dict = link_shopify_store_request_instance.to_dict()
# create an instance of LinkShopifyStoreRequest from a dict
link_shopify_store_request_form_dict = link_shopify_store_request.from_dict(link_shopify_store_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


