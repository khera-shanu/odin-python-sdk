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

from odin_sdk.models.secret_create import SecretCreate

class TestSecretCreate(unittest.TestCase):
    """SecretCreate unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SecretCreate:
        """Test SecretCreate
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SecretCreate`
        """
        model = SecretCreate()
        if include_optional:
            return SecretCreate(
                key = None,
                value = None,
                label = None,
                description = None
            )
        else:
            return SecretCreate(
                key = None,
                value = None,
        )
        """

    def testSecretCreate(self):
        """Test SecretCreate"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
