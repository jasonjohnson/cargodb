import logging
from cargo.wsgi.util import ok


LOG = logging.getLogger(__name__)


class ServerController(object):
    def GET(self):
        LOG.debug('fetching server status')
        return ok()
