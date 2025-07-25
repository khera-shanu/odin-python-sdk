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

from odin_sdk.models.fetch_similarities_for_content_key_request import FetchSimilaritiesForContentKeyRequest

class TestFetchSimilaritiesForContentKeyRequest(unittest.TestCase):
    """FetchSimilaritiesForContentKeyRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> FetchSimilaritiesForContentKeyRequest:
        """Test FetchSimilaritiesForContentKeyRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `FetchSimilaritiesForContentKeyRequest`
        """
        model = FetchSimilaritiesForContentKeyRequest()
        if include_optional:
            return FetchSimilaritiesForContentKeyRequest(
                project_id = None,
                document_key = None,
                similarity_threshold = None
            )
        else:
            return FetchSimilaritiesForContentKeyRequest(
                project_id = None,
                document_key = None,
        )
        """

    def testFetchSimilaritiesForContentKeyRequest(self):
        """Test FetchSimilaritiesForContentKeyRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
