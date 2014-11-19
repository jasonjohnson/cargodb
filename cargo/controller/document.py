import json
import logging
from cargo.wsgi.util import error, ok, not_found


LOG = logging.getLogger(__name__)


class DocumentController(object):
    def __init__(self, client):
        self.client = client

    def GET(self, db, doc):
        LOG.debug('with database %s fetching document %s' % (db, doc))

        document = self.client.doc_fetch(db, doc)

        if document:
            return ok(json.dumps({
                'document': document
            }))

        return not_found()

    def PUT(self, db, doc, content=None):
        LOG.debug('with database %s adding document %s' % (db, doc))

        if self.client.doc_save(db, doc, json.loads(content)):
            return ok()

        return error()

    def DELETE(self, db, doc):
        LOG.debug('with database %s deleting document %s' % (db, doc))

        if self.client.doc_delete(db, doc):
            return ok()

        return error()
