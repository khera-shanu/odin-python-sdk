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

from odin_sdk.models.chat_details import ChatDetails

class TestChatDetails(unittest.TestCase):
    """ChatDetails unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ChatDetails:
        """Test ChatDetails
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ChatDetails`
        """
        model = ChatDetails()
        if include_optional:
            return ChatDetails(
                updated_at = None,
                name = None,
                document_keys = None,
                created_by = None,
                metadata = None,
                created_at = None,
                id = None
            )
        else:
            return ChatDetails(
        )
        """

    def testChatDetails(self):
        """Test ChatDetails"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
