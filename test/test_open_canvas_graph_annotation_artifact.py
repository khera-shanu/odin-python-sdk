# coding: utf-8

"""
    API Docs

    API Documentation to interact with

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from odin_sdk.models.open_canvas_graph_annotation_artifact import OpenCanvasGraphAnnotationArtifact

class TestOpenCanvasGraphAnnotationArtifact(unittest.TestCase):
    """OpenCanvasGraphAnnotationArtifact unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> OpenCanvasGraphAnnotationArtifact:
        """Test OpenCanvasGraphAnnotationArtifact
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `OpenCanvasGraphAnnotationArtifact`
        """
        model = OpenCanvasGraphAnnotationArtifact()
        if include_optional:
            return OpenCanvasGraphAnnotationArtifact(
                current_index = None,
                contents = None
            )
        else:
            return OpenCanvasGraphAnnotationArtifact(
                current_index = None,
                contents = None,
        )
        """

    def testOpenCanvasGraphAnnotationArtifact(self):
        """Test OpenCanvasGraphAnnotationArtifact"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
