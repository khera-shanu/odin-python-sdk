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

from odin_sdk.models.resource_type_id1 import ResourceTypeId1

class TestResourceTypeId1(unittest.TestCase):
    """ResourceTypeId1 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ResourceTypeId1:
        """Test ResourceTypeId1
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ResourceTypeId1`
        """
        model = ResourceTypeId1()
        if include_optional:
            return ResourceTypeId1(
            )
        else:
            return ResourceTypeId1(
        )
        """

    def testResourceTypeId1(self):
        """Test ResourceTypeId1"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
