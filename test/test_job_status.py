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

from odin_sdk.models.job_status import JobStatus

class TestJobStatus(unittest.TestCase):
    """JobStatus unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> JobStatus:
        """Test JobStatus
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `JobStatus`
        """
        model = JobStatus()
        if include_optional:
            return JobStatus(
                job_type = None,
                uid = None,
                document_keys = None,
                job_id = None,
                use_job_id_path = None,
                job_name = None,
                last_updated = None,
                job_status = None,
                project_id = None,
                result_type = None,
                credits_used = None,
                extra_info = None
            )
        else:
            return JobStatus(
                job_type = None,
                uid = None,
                document_keys = None,
                job_id = None,
                use_job_id_path = None,
                job_name = None,
                last_updated = None,
                job_status = None,
                project_id = None,
                result_type = None,
        )
        """

    def testJobStatus(self):
        """Test JobStatus"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
