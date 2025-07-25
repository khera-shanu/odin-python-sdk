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

from odin_sdk.models.model_update import ModelUpdate

class TestModelUpdate(unittest.TestCase):
    """ModelUpdate unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ModelUpdate:
        """Test ModelUpdate
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ModelUpdate`
        """
        model = ModelUpdate()
        if include_optional:
            return ModelUpdate(
                model_name = None,
                api_url = None,
                api_type = None,
                max_input_tokens = None,
                max_response_tokens = None,
                display_name = None,
                cost = None,
                hidden = None,
                api_key = None,
                api_version = None,
                is_default = None,
                is_default_extraction_model = None,
                is_default_citation_model = None,
                model_extra_params = None
            )
        else:
            return ModelUpdate(
                model_name = None,
                api_url = None,
                api_type = None,
                max_input_tokens = None,
                max_response_tokens = None,
                display_name = None,
                cost = None,
        )
        """

    def testModelUpdate(self):
        """Test ModelUpdate"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
