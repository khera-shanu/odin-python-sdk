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

from odin_sdk.models.debug import Debug

class TestDebug(unittest.TestCase):
    """Debug unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Debug:
        """Test Debug
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Debug`
        """
        model = Debug()
        if include_optional:
            return Debug(
            )
        else:
            return Debug(
        )
        """

    def testDebug(self):
        """Test Debug"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
