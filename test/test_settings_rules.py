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

from odin_sdk.models.settings_rules import SettingsRules

class TestSettingsRules(unittest.TestCase):
    """SettingsRules unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SettingsRules:
        """Test SettingsRules
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SettingsRules`
        """
        model = SettingsRules()
        if include_optional:
            return SettingsRules(
                view = None,
                edit = None
            )
        else:
            return SettingsRules(
        )
        """

    def testSettingsRules(self):
        """Test SettingsRules"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
