import json
import logging
from cargo.wsgi.util import error, ok, not_found


LOG = logging.getLogger(__name__)


class DatabaseController(object):
    def __init__(self, client):
        self.client = client

    def GET(self, db):
        LOG.debug('fetching database %s', db)

        documents = self.client.db_fetch(db)

        if documents:
            return ok(json.dumps({
                'documents': self.client.db_fetch(db)
            }))

        return not_found()

    def PUT(self, db):
        LOG.debug('adding database %s' % db)

        if self.client.db_init(db):
            return ok()

        return error()

    def DELETE(self, db):
        LOG.debug('deleting database %s' % db)

        if self.client.db_delete(db):
            return ok()

        return error()
