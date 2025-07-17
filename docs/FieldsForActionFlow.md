# FieldsForActionFlow


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info_key** | **object** | The key/variable name for the field. For example, &#39;destination_email&#39;. | 
**description** | **object** | The description of the field for the LLM. For example, &#39;The email address to send the report to.&#39; | 
**default_from** | **object** | Explanation of where to take the default value from for the LLM. For example, &#39;User&#39;s messages.&#39; | 
**required** | **object** | Whether the field is required or not. | 
**hr_name** | **object** | The human readable name of the field. For example, &#39;Destination Email&#39;. | 
**provide_as** | [**ProvideAs**](ProvideAs.md) |  | [optional] 
**default_value** | [**DefaultValue1**](DefaultValue1.md) |  | [optional] 
**dropdown_details** | [**DropdownDetails**](DropdownDetails.md) |  | [optional] 

## Example

```python
from odin_sdk.models.fields_for_action_flow import FieldsForActionFlow

# TODO update the JSON string below
json = "{}"
# create an instance of FieldsForActionFlow from a JSON string
fields_for_action_flow_instance = FieldsForActionFlow.from_json(json)
# print the JSON string representation of the object
print FieldsForActionFlow.to_json()

# convert the object into a dict
fields_for_action_flow_dict = fields_for_action_flow_instance.to_dict()
# create an instance of FieldsForActionFlow from a dict
fields_for_action_flow_form_dict = fields_for_action_flow.from_dict(fields_for_action_flow_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


