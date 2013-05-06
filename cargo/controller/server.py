from cargo.wsgi.util import ok


class ServerController(object):
    def GET(self):
        return ok({'status': 'OK', 'version': 0.1})
