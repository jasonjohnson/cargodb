from cargo.controller import ServerController, DatabaseController, \
                             DocumentController
from cargo.middleware import Router
from cargo.wsgi import Request, Response


def application(env, start_response):
    router = Router(Request(env), Response())

    # Add our controllers
    router.add_controller(ServerController)   # /
    router.add_controller(DatabaseController) # /{db}
    router.add_controller(DocumentController) # /{db}/{doc_id}

    # Finally, dispatch the request into the controller stack.
    return router.dispatch()(env, start_response)


if __name__ == '__main__':
    from wsgiref.simple_server import make_server

    httpd = make_server('', 8080, application)
    httpd.serve_forever()
