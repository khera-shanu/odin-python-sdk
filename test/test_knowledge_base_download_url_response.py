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

from odin_sdk.models.knowledge_base_download_url_response import KnowledgeBaseDownloadUrlResponse

class TestKnowledgeBaseDownloadUrlResponse(unittest.TestCase):
    """KnowledgeBaseDownloadUrlResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> KnowledgeBaseDownloadUrlResponse:
        """Test KnowledgeBaseDownloadUrlResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `KnowledgeBaseDownloadUrlResponse`
        """
        model = KnowledgeBaseDownloadUrlResponse()
        if include_optional:
            return KnowledgeBaseDownloadUrlResponse(
                download_url = None,
                metadata_url = None
            )
        else:
            return KnowledgeBaseDownloadUrlResponse(
                download_url = None,
        )
        """

    def testKnowledgeBaseDownloadUrlResponse(self):
        """Test KnowledgeBaseDownloadUrlResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
