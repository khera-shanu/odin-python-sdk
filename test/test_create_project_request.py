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

from odin_sdk.models.create_project_request import CreateProjectRequest

class TestCreateProjectRequest(unittest.TestCase):
    """CreateProjectRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CreateProjectRequest:
        """Test CreateProjectRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CreateProjectRequest`
        """
        model = CreateProjectRequest()
        if include_optional:
            return CreateProjectRequest(
                project_name = None,
                project_description = None,
                project_type = None,
                personality_name = None,
                personality_instructions = None,
                personality_id = None,
                personality_type = None,
                personality_temperature = None
            )
        else:
            return CreateProjectRequest(
                project_name = None,
                project_description = None,
        )
        """

    def testCreateProjectRequest(self):
        """Test CreateProjectRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
