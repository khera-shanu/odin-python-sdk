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

from odin_sdk.models.ai_summarize_request import AISummarizeRequest

class TestAISummarizeRequest(unittest.TestCase):
    """AISummarizeRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AISummarizeRequest:
        """Test AISummarizeRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AISummarizeRequest`
        """
        model = AISummarizeRequest()
        if include_optional:
            return AISummarizeRequest(
                text = None,
                project_id = None,
                instructions = None
            )
        else:
            return AISummarizeRequest(
                text = None,
                project_id = None,
                instructions = None,
        )
        """

    def testAISummarizeRequest(self):
        """Test AISummarizeRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
