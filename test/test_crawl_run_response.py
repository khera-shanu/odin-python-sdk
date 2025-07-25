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

from odin_sdk.models.crawl_run_response import CrawlRunResponse

class TestCrawlRunResponse(unittest.TestCase):
    """CrawlRunResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CrawlRunResponse:
        """Test CrawlRunResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CrawlRunResponse`
        """
        model = CrawlRunResponse()
        if include_optional:
            return CrawlRunResponse(
                id = None,
                crawl_config_id = None,
                created_at = None,
                updated_at = None,
                status = None,
                error_message = None,
                error_traceback = None,
                error_occurred = None,
                error_occurred_at = None
            )
        else:
            return CrawlRunResponse(
                id = None,
                crawl_config_id = None,
                created_at = None,
                updated_at = None,
                status = None,
                error_message = None,
                error_traceback = None,
                error_occurred = None,
                error_occurred_at = None,
        )
        """

    def testCrawlRunResponse(self):
        """Test CrawlRunResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
