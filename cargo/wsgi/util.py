def ok(content=None):
    return ('200 OK', content)


def error(content=None):
    return ('500 Error', content)


def not_found(content=None):
    return ('404 Not Found', content)
