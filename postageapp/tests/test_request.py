from unittest import TestCase
from pprint import pprint

import json
import postageapp

from postageapp import Request

class TestRequest(TestCase):
    def test_empty_request(self):
        request = Request()

        self.assertTrue(isinstance(request, Request))

    def test_make_request(self):
        request = Request()

        pprint(request.send())
