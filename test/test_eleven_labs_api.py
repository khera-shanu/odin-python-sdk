# coding: utf-8

"""
    API Docs

    API Documentation to interact with

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from odin_sdk.api.eleven_labs_api import ElevenLabsApi


class TestElevenLabsApi(unittest.TestCase):
    """ElevenLabsApi unit test stubs"""

    def setUp(self) -> None:
        self.api = ElevenLabsApi()

    def tearDown(self) -> None:
        pass

    def test_edit_agent_elevenlabs_agent_edit_post(self) -> None:
        """Test case for edit_agent_elevenlabs_agent_edit_post

        Edit Agent
        """
        pass

    def test_get_signed_url_elevenlabs_signed_url_get(self) -> None:
        """Test case for get_signed_url_elevenlabs_signed_url_get

        Get Signed Url
        """
        pass

    def test_save_voice_conversation_pair_elevenlabs_voice_conversation_save_pair_post(self) -> None:
        """Test case for save_voice_conversation_pair_elevenlabs_voice_conversation_save_pair_post

        Save Voice Conversation Pair
        """
        pass

    def test_save_voice_message_elevenlabs_voice_message_save_post(self) -> None:
        """Test case for save_voice_message_elevenlabs_voice_message_save_post

        Save Voice Message
        """
        pass


if __name__ == '__main__':
    unittest.main()
