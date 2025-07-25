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

from odin_sdk.models.save_action_request import SaveActionRequest

class TestSaveActionRequest(unittest.TestCase):
    """SaveActionRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SaveActionRequest:
        """Test SaveActionRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SaveActionRequest`
        """
        model = SaveActionRequest()
        if include_optional:
            return SaveActionRequest(
                project_id = None,
                flow_id = None,
                action_name = None,
                action_description = None,
                required_fields_for_flow = None,
                is_test = None,
                confirm_button_label = None,
                cancel_button_label = None,
                autosend = None,
                type = None,
                config = None
            )
        else:
            return SaveActionRequest(
                project_id = None,
                flow_id = None,
                action_name = None,
                action_description = None,
        )
        """

    def testSaveActionRequest(self):
        """Test SaveActionRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
