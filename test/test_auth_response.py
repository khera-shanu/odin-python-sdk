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

from odin_sdk.models.auth_response import AuthResponse

class TestAuthResponse(unittest.TestCase):
    """AuthResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AuthResponse:
        """Test AuthResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AuthResponse`
        """
        model = AuthResponse()
        if include_optional:
            return AuthResponse(
                kind = None,
                id_token = None,
                refresh_token = None,
                expires_in = None,
                is_new_user = None
            )
        else:
            return AuthResponse(
                kind = None,
                id_token = None,
                refresh_token = None,
                expires_in = None,
                is_new_user = None,
        )
        """

    def testAuthResponse(self):
        """Test AuthResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
