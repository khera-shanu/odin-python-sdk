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

from odin_sdk.models.doc1_content import Doc1Content

class TestDoc1Content(unittest.TestCase):
    """Doc1Content unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Doc1Content:
        """Test Doc1Content
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Doc1Content`
        """
        model = Doc1Content()
        if include_optional:
            return Doc1Content(
            )
        else:
            return Doc1Content(
        )
        """

    def testDoc1Content(self):
        """Test Doc1Content"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
