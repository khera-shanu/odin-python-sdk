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

from odin_sdk.models.building_blocks import BuildingBlocks

class TestBuildingBlocks(unittest.TestCase):
    """BuildingBlocks unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> BuildingBlocks:
        """Test BuildingBlocks
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `BuildingBlocks`
        """
        model = BuildingBlocks()
        if include_optional:
            return BuildingBlocks(
            )
        else:
            return BuildingBlocks(
        )
        """

    def testBuildingBlocks(self):
        """Test BuildingBlocks"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
