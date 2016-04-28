class Config:
    def __init__(self):
        self._host = 'api.postageapp.com'
        self._proto = 'https'
        self._port = None
        self._api_key = None
        self._environment = None
        self._framework = 'Python'

    @property
    def host(self):
        return self._host

    @property
    def proto(self):
        return self._proto

    @property
    def port(self):
        return self._port

    @property
    def api_key(self):
        return self._api_key

    @property
    def environment(self):
        return self._environment

    @property
    def framework(self):
        return self._framework
