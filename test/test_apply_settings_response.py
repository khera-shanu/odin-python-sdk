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

from odin_sdk.models.apply_settings_response import ApplySettingsResponse

class TestApplySettingsResponse(unittest.TestCase):
    """ApplySettingsResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ApplySettingsResponse:
        """Test ApplySettingsResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ApplySettingsResponse`
        """
        model = ApplySettingsResponse()
        if include_optional:
            return ApplySettingsResponse(
                success = None,
                message = None,
                job_id = None,
                sync_status = None
            )
        else:
            return ApplySettingsResponse(
                success = None,
                message = None,
                sync_status = None,
        )
        """

    def testApplySettingsResponse(self):
        """Test ApplySettingsResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
