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

from odin_sdk.models.fields_for_action_flow import FieldsForActionFlow

class TestFieldsForActionFlow(unittest.TestCase):
    """FieldsForActionFlow unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> FieldsForActionFlow:
        """Test FieldsForActionFlow
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `FieldsForActionFlow`
        """
        model = FieldsForActionFlow()
        if include_optional:
            return FieldsForActionFlow(
                info_key = None,
                description = None,
                default_from = None,
                required = None,
                hr_name = None,
                provide_as = None,
                default_value = None,
                dropdown_details = None
            )
        else:
            return FieldsForActionFlow(
                info_key = None,
                description = None,
                default_from = None,
                required = None,
                hr_name = None,
        )
        """

    def testFieldsForActionFlow(self):
        """Test FieldsForActionFlow"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
