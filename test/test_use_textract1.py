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

from odin_sdk.models.use_textract1 import UseTextract1

class TestUseTextract1(unittest.TestCase):
    """UseTextract1 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> UseTextract1:
        """Test UseTextract1
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `UseTextract1`
        """
        model = UseTextract1()
        if include_optional:
            return UseTextract1(
            )
        else:
            return UseTextract1(
        )
        """

    def testUseTextract1(self):
        """Test UseTextract1"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
