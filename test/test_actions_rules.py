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

from odin_sdk.models.actions_rules import ActionsRules

class TestActionsRules(unittest.TestCase):
    """ActionsRules unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ActionsRules:
        """Test ActionsRules
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ActionsRules`
        """
        model = ActionsRules()
        if include_optional:
            return ActionsRules(
                view = None,
                edit = None
            )
        else:
            return ActionsRules(
        )
        """

    def testActionsRules(self):
        """Test ActionsRules"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
