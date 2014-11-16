class Response(object):
    def __init__(self):
        self.status = '200 OK'
        self.headers = {}
        self.length = 0
        self.body = None

    def set_header(self, name, value):
        self.headers[name] = str(value)

    def set_status(self, value):
        self.status = value

    def set_body(self, body):
        self.body = body
        self.length = len(self.body)

    def __call__(self, env, start_response):
        self.set_header('Content-Length', self.length)

        start_response(self.status, self.headers.items())

        if not self.body or not self.length:
            return []

        return [self.body]
