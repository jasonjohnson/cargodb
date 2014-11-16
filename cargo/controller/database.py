import logging
from cargo.wsgi.util import ok


LOG = logging.getLogger(__name__)


class DatabaseController(object):
    def GET(self, db):
        LOG.debug('fetching database %s', db)
        return ok()

    def PUT(self, db):
        LOG.debug('adding database %s' % db)
        return ok()

    def DELETE(self, db):
        LOG.debug('deleting database %s' % db)
        return ok()
