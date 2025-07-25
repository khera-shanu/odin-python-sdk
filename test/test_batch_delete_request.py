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

from odin_sdk.models.batch_delete_request import BatchDeleteRequest

class TestBatchDeleteRequest(unittest.TestCase):
    """BatchDeleteRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> BatchDeleteRequest:
        """Test BatchDeleteRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `BatchDeleteRequest`
        """
        model = BatchDeleteRequest()
        if include_optional:
            return BatchDeleteRequest(
                project_id = None,
                resources = None
            )
        else:
            return BatchDeleteRequest(
                project_id = None,
                resources = None,
        )
        """

    def testBatchDeleteRequest(self):
        """Test BatchDeleteRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
