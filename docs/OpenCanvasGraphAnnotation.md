# OpenCanvasGraphAnnotation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**highlighted_code** | [**OpenCanvasGraphAnnotationHighlightedCode**](OpenCanvasGraphAnnotationHighlightedCode.md) |  | [optional] 
**highlighted_text** | [**OpenCanvasGraphAnnotationHighlightedText**](OpenCanvasGraphAnnotationHighlightedText.md) |  | [optional] 
**artifact** | [**OpenCanvasGraphAnnotationArtifact**](OpenCanvasGraphAnnotationArtifact.md) |  | [optional] 
**next** | [**Next**](Next.md) |  | [optional] 
**language** | [**OpenCanvasGraphAnnotationLanguage**](OpenCanvasGraphAnnotationLanguage.md) |  | [optional] 
**artifact_length** | [**OpenCanvasGraphAnnotationArtifactLength**](OpenCanvasGraphAnnotationArtifactLength.md) |  | [optional] 
**regenerate_with_emojis** | [**RegenerateWithEmojis**](RegenerateWithEmojis.md) |  | [optional] 
**reading_level** | [**OpenCanvasGraphAnnotationReadingLevel**](OpenCanvasGraphAnnotationReadingLevel.md) |  | [optional] 
**add_comments** | [**AddComments**](AddComments.md) |  | [optional] 
**add_logs** | [**AddLogs**](AddLogs.md) |  | [optional] 
**port_language** | [**CodeHighlightLanguage**](CodeHighlightLanguage.md) |  | [optional] 
**fix_bugs** | [**FixBugs**](FixBugs.md) |  | [optional] 
**custom_quick_action_id** | [**CustomQuickActionId**](CustomQuickActionId.md) |  | [optional] 

## Example

```python
from odin_sdk.models.open_canvas_graph_annotation import OpenCanvasGraphAnnotation

# TODO update the JSON string below
json = "{}"
# create an instance of OpenCanvasGraphAnnotation from a JSON string
open_canvas_graph_annotation_instance = OpenCanvasGraphAnnotation.from_json(json)
# print the JSON string representation of the object
print OpenCanvasGraphAnnotation.to_json()

# convert the object into a dict
open_canvas_graph_annotation_dict = open_canvas_graph_annotation_instance.to_dict()
# create an instance of OpenCanvasGraphAnnotation from a dict
open_canvas_graph_annotation_form_dict = open_canvas_graph_annotation.from_dict(open_canvas_graph_annotation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


