
class Request:
    def __init__(self):
        self.action = 'send_message'

    @property
    def action(self):
        return self._action

    @action.setter
    def action(self, _action):
        self._action = _action

        return self._action

    def send(self):
        return

