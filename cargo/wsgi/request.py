class Request(object):
    def __init__(self, env):
        self.env = env
        self.path = self._path()
        self.method = self._method()
        self.length = self._length()
        self.body = self._body()

    def _path(self):
        pieces = self.env.get('PATH_INFO').split('/')
        pieces.pop(0)

        return [] if not pieces[0] else pieces

    def _method(self):
        return self.env.get('REQUEST_METHOD')

    def _length(self):
        return self.env.get('CONTENT_LENGTH')

    def _body(self):
        if not self.length:
            return None

        body = self.env.get('wsgi.input')
        body = body.read(int(self.length))

        return body
