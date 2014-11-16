import logging
from cargo.controller import (ServerController, DatabaseController,
                              DocumentController)
from cargo.wsgi import Router, Request, Response


logging.basicConfig(level=logging.DEBUG)

LOG = logging.getLogger(__name__)


def application(env, start_response):
    router = Router(Request(env), Response())

    router.add_controller(ServerController())
    router.add_controller(DatabaseController())
    router.add_controller(DocumentController())

    return router.dispatch()(env, start_response)


def main():
    from wsgiref.simple_server import make_server

    LOG.debug('starting wsgiref server')
    httpd = make_server('', 8080, application)
    httpd.serve_forever()
