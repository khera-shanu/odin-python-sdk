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

from odin_sdk.models.response_execute_action_on_form_actions_execute_post import ResponseExecuteActionOnFormActionsExecutePost

class TestResponseExecuteActionOnFormActionsExecutePost(unittest.TestCase):
    """ResponseExecuteActionOnFormActionsExecutePost unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ResponseExecuteActionOnFormActionsExecutePost:
        """Test ResponseExecuteActionOnFormActionsExecutePost
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ResponseExecuteActionOnFormActionsExecutePost`
        """
        model = ResponseExecuteActionOnFormActionsExecutePost()
        if include_optional:
            return ResponseExecuteActionOnFormActionsExecutePost(
                message = None,
                success = None,
                chat_id = None,
                message_id = None,
                flow_run_id = None,
                action_response = None
            )
        else:
            return ResponseExecuteActionOnFormActionsExecutePost(
                message = None,
                success = None,
        )
        """

    def testResponseExecuteActionOnFormActionsExecutePost(self):
        """Test ResponseExecuteActionOnFormActionsExecutePost"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
