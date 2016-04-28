import requests

import postageapp

class Request:
    def __init__(self):
        self._method = 'send_message'
        self._body = { }

    @property
    def method(self):
        return self._method

    @method.setter
    def method(self, _method):
        self._method = _method

        return self._method

    @property
    def body(self):
        self.body

    @body.setter
    def body(self, _body):
        self._body = _body

    def endpoint(self):
        if (postageapp.config.port):
            return "%s://%s:%d/v.1.0/%s" % (
                postageapp.config.proto,
                postageapp.config.host,
                postageapp.config.port,
                self.method
            )
        else:
            return "%s://%s/v.1.0/%s" % (
                postageapp.config.proto,
                postageapp.config.host,
                self.method
            )

    def send(self):
        r = requests.post(self.endpoint(), json=self._body)
        return r.json()
