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

from odin_sdk.models.agent_difficulty_level_response import AgentDifficultyLevelResponse

class TestAgentDifficultyLevelResponse(unittest.TestCase):
    """AgentDifficultyLevelResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AgentDifficultyLevelResponse:
        """Test AgentDifficultyLevelResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AgentDifficultyLevelResponse`
        """
        model = AgentDifficultyLevelResponse()
        if include_optional:
            return AgentDifficultyLevelResponse(
                difficulty_level = None
            )
        else:
            return AgentDifficultyLevelResponse(
                difficulty_level = None,
        )
        """

    def testAgentDifficultyLevelResponse(self):
        """Test AgentDifficultyLevelResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
