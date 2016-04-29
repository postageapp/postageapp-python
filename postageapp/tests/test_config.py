from unittest import TestCase

import postageapp
import os

from postageapp import Config

class TestConfig(TestCase):
    def test_default_config(self):
        config = Config()

        self.assertTrue(isinstance(config, Config))

    def test_api_key_assigned(self):
        config = Config()

        self.assertTrue(
            isinstance(config.api_key, basestring),
            'The POSTAGEAPP_API_KEY environment variable needs to be assigned with a valid key to do testing.'
        )
        self.assertEqual(
            len(config.api_key), 32,
            'The assigned POSTAGEAPP_API_KEY environment variable is the wrong length.'
        )
