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

from odin_sdk.models.credits_used1 import CreditsUsed1

class TestCreditsUsed1(unittest.TestCase):
    """CreditsUsed1 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CreditsUsed1:
        """Test CreditsUsed1
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CreditsUsed1`
        """
        model = CreditsUsed1()
        if include_optional:
            return CreditsUsed1(
            )
        else:
            return CreditsUsed1(
        )
        """

    def testCreditsUsed1(self):
        """Test CreditsUsed1"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
