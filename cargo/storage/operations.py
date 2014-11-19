import logging
import os
import shelve


LOG = logging.getLogger(__name__)

PATH = '/tmp'

DATABASES = {}


def db_fetch(db):
    LOG.debug('fetching database %s' % db)

    if db in DATABASES:
        return DATABASES[db].keys()

    return False


def db_init(db):
    LOG.debug('initializing database %s' % db)

    if db not in DATABASES:
        LOG.debug('opening database %s' % db)
        DATABASES[db] = shelve.open('%s/%s' % (PATH, db), writeback=True)

    return True


def db_delete(db):
    LOG.debug('deleting database %s' % db)

    if db in DATABASES:
        DATABASES[db].close()
        DATABASES.pop(db, None)

        os.remove('%s/%s' % (PATH, db))
        return True

    LOG.debug('tried to delete unknown database %s' % db)
    return False


def doc_fetch(db, doc):
    LOG.debug('with database %s fetching document %s' % (db, doc))
    db_init(db)
    return DATABASES[db].get(doc, False)


def doc_save(db, doc, content):
    LOG.debug('with database %s saving document %s' % (db, doc))
    db_init(db)
    DATABASES[db][doc] = content
    DATABASES[db].sync()
    return True


def doc_delete(db, doc):
    LOG.debug('with database %s deleting document %s' % (db, doc))
    db_init(db)
    doc = DATABASES[db].pop(doc, None)

    if not doc:
        return False

    DATABASES[db].sync()
    return True
