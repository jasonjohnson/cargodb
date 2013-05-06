import json


class Request(object):
    def __init__(self, env):
        self.env = env
        self.content_type = self._content_type()
        self.path = self._path()
        self.method = self._method()
        self.length = self._length()
        self.body = self._body()

    def is_json(self):
        return self.content_type == 'application/json'

    def _path(self):
        pieces = self.env.get('PATH_INFO').split('/')
        pieces.pop(0)

        return [] if not pieces[0] else pieces

    def _method(self):
        return self.env.get('REQUEST_METHOD')

    def _length(self):
        return self.env.get('CONTENT_LENGTH')

    def _content_type(self):
        return self.env.get('CONTENT_TYPE')

    def _body(self):
        if not self.length:
            return None

        body = self.env.get('wsgi.input')
        body = body.read(int(self.length))

        if self.is_json():
            body = json.loads(body)

        return body
