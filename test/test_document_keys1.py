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

from odin_sdk.models.document_keys1 import DocumentKeys1

class TestDocumentKeys1(unittest.TestCase):
    """DocumentKeys1 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DocumentKeys1:
        """Test DocumentKeys1
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DocumentKeys1`
        """
        model = DocumentKeys1()
        if include_optional:
            return DocumentKeys1(
            )
        else:
            return DocumentKeys1(
        )
        """

    def testDocumentKeys1(self):
        """Test DocumentKeys1"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
