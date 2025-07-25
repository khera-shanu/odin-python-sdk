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

from odin_sdk.models.import_tool_request import ImportToolRequest

class TestImportToolRequest(unittest.TestCase):
    """ImportToolRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ImportToolRequest:
        """Test ImportToolRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ImportToolRequest`
        """
        model = ImportToolRequest()
        if include_optional:
            return ImportToolRequest(
                tool_data = None,
                project_id = None,
                new_name = None,
                import_as_draft = None
            )
        else:
            return ImportToolRequest(
                tool_data = None,
                project_id = None,
        )
        """

    def testImportToolRequest(self):
        """Test ImportToolRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
