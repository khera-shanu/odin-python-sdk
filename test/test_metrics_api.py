# coding: utf-8

"""
    API Docs

    API Documentation to interact with

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from odin_sdk.api.metrics_api import MetricsApi


class TestMetricsApi(unittest.TestCase):
    """MetricsApi unit test stubs"""

    def setUp(self) -> None:
        self.api = MetricsApi()

    def tearDown(self) -> None:
        pass

    def test_get_chart_metrics_metrics_charts_get(self) -> None:
        """Test case for get_chart_metrics_metrics_charts_get

        Get Chart Metrics
        """
        pass

    def test_get_tools_metrics_metrics_get(self) -> None:
        """Test case for get_tools_metrics_metrics_get

        Get Tools Metrics
        """
        pass


if __name__ == '__main__':
    unittest.main()
