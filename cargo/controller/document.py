import logging
from cargo.wsgi.util import ok


LOG = logging.getLogger(__name__)


class DocumentController(object):
    def GET(self, db, doc):
        LOG.debug('with database %s fetching document %s' % (db, doc))
        return ok()

    def PUT(self, db, doc, content=None):
        LOG.debug('with database %s adding document %s' % (db, doc))
        return ok()

    def DELETE(self, db, doc):
        LOG.debug('with database %s deleting document %s' % (db, doc))
        return ok()
