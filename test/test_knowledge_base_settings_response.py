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

from odin_sdk.models.knowledge_base_settings_response import KnowledgeBaseSettingsResponse

class TestKnowledgeBaseSettingsResponse(unittest.TestCase):
    """KnowledgeBaseSettingsResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> KnowledgeBaseSettingsResponse:
        """Test KnowledgeBaseSettingsResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `KnowledgeBaseSettingsResponse`
        """
        model = KnowledgeBaseSettingsResponse()
        if include_optional:
            return KnowledgeBaseSettingsResponse(
                success = None,
                data = None,
                message = None
            )
        else:
            return KnowledgeBaseSettingsResponse(
                success = None,
                message = None,
        )
        """

    def testKnowledgeBaseSettingsResponse(self):
        """Test KnowledgeBaseSettingsResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
