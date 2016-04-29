from unittest import TestCase
from pprint import pprint

import json
import postageapp

from postageapp import Request

class TestRequest(TestCase):
    def test_empty_request(self):
        request = Request()

        self.assertTrue(isinstance(request, Request))
        self.assertEqual(request.method, 'send_message')

    def test_request_project_info(self):
        request = Request('get_project_info')

        result = request.send()

        self.assertTrue(result['data'])

    def test_send_message(self):
        request = Request()

        request.arguments.recipients = 'test@postageapp.com'
        request.arguments.deliver = False

        result = request.send()

        self.assertTrue(result['data'])
