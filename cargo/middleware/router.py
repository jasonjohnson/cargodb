class Router(object):
    def __init__(self, request, response):
        self.request = request
        self.response = response
        self.controllers = []

    def add_controller(self, controller):
        self.controllers.append(controller)

    def controller(self):
        return self.controllers[len(self.args())]

    def method(self):
        return self.request.method

    def args(self):
        return self.request.path

    def dispatch(self):
        controller = self.controller()
        method = self.method()
        args = self.args()

        # If the request normally has a body, the controller
        # is going to expect it as an argument.
        if self.request.body:
            args.append(self.request.body)

        status, body = getattr(controller(), method)(*args)

        self.response.set_status(status)
        self.response.set_body(body)

        return self.response
