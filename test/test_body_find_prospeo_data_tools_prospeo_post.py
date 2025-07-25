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

from odin_sdk.models.body_find_prospeo_data_tools_prospeo_post import BodyFindProspeoDataToolsProspeoPost

class TestBodyFindProspeoDataToolsProspeoPost(unittest.TestCase):
    """BodyFindProspeoDataToolsProspeoPost unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> BodyFindProspeoDataToolsProspeoPost:
        """Test BodyFindProspeoDataToolsProspeoPost
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `BodyFindProspeoDataToolsProspeoPost`
        """
        model = BodyFindProspeoDataToolsProspeoPost()
        if include_optional:
            return BodyFindProspeoDataToolsProspeoPost(
                req = odin_sdk.models.prospeo_request.ProspeoRequest(
                    api_type = null, ),
                domain_search = odin_sdk.models.domain_search_request.DomainSearchRequest(
                    company = null, 
                    limit = null, 
                    email_type = null, 
                    company_enrichment = null, ),
                email_finder = odin_sdk.models.email_finder_request.EmailFinderRequest(
                    first_name = null, 
                    last_name = null, 
                    full_name = null, 
                    company = null, ),
                linkedin_email_finder = odin_sdk.models.linked_in_email_finder_request.LinkedInEmailFinderRequest(
                    url = null, 
                    profile_only = null, ),
                email_verifier = odin_sdk.models.email_verifier_request.EmailVerifierRequest(
                    email = null, 
                    email_anon_id = null, )
            )
        else:
            return BodyFindProspeoDataToolsProspeoPost(
                req = odin_sdk.models.prospeo_request.ProspeoRequest(
                    api_type = null, ),
        )
        """

    def testBodyFindProspeoDataToolsProspeoPost(self):
        """Test BodyFindProspeoDataToolsProspeoPost"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
