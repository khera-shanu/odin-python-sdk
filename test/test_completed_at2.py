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

from odin_sdk.models.completed_at2 import CompletedAt2

class TestCompletedAt2(unittest.TestCase):
    """CompletedAt2 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CompletedAt2:
        """Test CompletedAt2
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CompletedAt2`
        """
        model = CompletedAt2()
        if include_optional:
            return CompletedAt2(
            )
        else:
            return CompletedAt2(
        )
        """

    def testCompletedAt2(self):
        """Test CompletedAt2"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
