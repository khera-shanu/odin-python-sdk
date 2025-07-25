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

from odin_sdk.models.create_project_response import CreateProjectResponse

class TestCreateProjectResponse(unittest.TestCase):
    """CreateProjectResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CreateProjectResponse:
        """Test CreateProjectResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CreateProjectResponse`
        """
        model = CreateProjectResponse()
        if include_optional:
            return CreateProjectResponse(
                project_id = None,
                project = odin_sdk.models.project_info.ProjectInfo(
                    name = null, 
                    created_at = null, 
                    members = null, 
                    owner = null, 
                    description = null, 
                    type = null, 
                    model_name = null, 
                    system_prompt = null, 
                    id = null, )
            )
        else:
            return CreateProjectResponse(
                project_id = None,
                project = odin_sdk.models.project_info.ProjectInfo(
                    name = null, 
                    created_at = null, 
                    members = null, 
                    owner = null, 
                    description = null, 
                    type = null, 
                    model_name = null, 
                    system_prompt = null, 
                    id = null, ),
        )
        """

    def testCreateProjectResponse(self):
        """Test CreateProjectResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
