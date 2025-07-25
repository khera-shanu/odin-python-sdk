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

from odin_sdk.models.custom_tool_response import CustomToolResponse

class TestCustomToolResponse(unittest.TestCase):
    """CustomToolResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CustomToolResponse:
        """Test CustomToolResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CustomToolResponse`
        """
        model = CustomToolResponse()
        if include_optional:
            return CustomToolResponse(
                id = None,
                name = None,
                description = None,
                inputs = {
                    'key' : odin_sdk.models.tool_input.ToolInput(
                        id = null, 
                        type = null, 
                        value = null, 
                        manual_input = null, 
                        description = null, )
                    },
                steps = {
                    'key' : odin_sdk.models.tool_step.ToolStep(
                        id = null, 
                        tool_id = null, 
                        type = null, 
                        label = null, 
                        description = null, 
                        settings = null, )
                    },
                test_step_results = None,
                project_id = None,
                created_by = None,
                created_at = None,
                updated_at = None,
                is_published = None,
                version = None,
                published_at = None,
                is_draft = None,
                is_public = None
            )
        else:
            return CustomToolResponse(
                id = None,
                name = None,
                inputs = {
                    'key' : odin_sdk.models.tool_input.ToolInput(
                        id = null, 
                        type = null, 
                        value = null, 
                        manual_input = null, 
                        description = null, )
                    },
                steps = {
                    'key' : odin_sdk.models.tool_step.ToolStep(
                        id = null, 
                        tool_id = null, 
                        type = null, 
                        label = null, 
                        description = null, 
                        settings = null, )
                    },
                project_id = None,
                created_by = None,
                created_at = None,
                updated_at = None,
                is_published = None,
                is_draft = None,
                is_public = None,
        )
        """

    def testCustomToolResponse(self):
        """Test CustomToolResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
