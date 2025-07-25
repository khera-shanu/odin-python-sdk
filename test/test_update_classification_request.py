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

from odin_sdk.models.update_classification_request import UpdateClassificationRequest

class TestUpdateClassificationRequest(unittest.TestCase):
    """UpdateClassificationRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> UpdateClassificationRequest:
        """Test UpdateClassificationRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `UpdateClassificationRequest`
        """
        model = UpdateClassificationRequest()
        if include_optional:
            return UpdateClassificationRequest(
                classification_id = None,
                data = odin_sdk.models.classification.Classification(
                    project_id = null, 
                    title = null, 
                    flow = null, )
            )
        else:
            return UpdateClassificationRequest(
                classification_id = None,
                data = odin_sdk.models.classification.Classification(
                    project_id = null, 
                    title = null, 
                    flow = null, ),
        )
        """

    def testUpdateClassificationRequest(self):
        """Test UpdateClassificationRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
