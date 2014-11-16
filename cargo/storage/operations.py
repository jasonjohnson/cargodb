import logging
import os
import shelve


LOG = logging.getLogger(__name__)

PATH = '/tmp'

DATABASES = {}


def db_fetch(db):
    LOG.debug('fetching database %s' % db)
    print(DATABASES[db].keys())


def db_init(db):
    LOG.debug('initializing database %s' % db)

    if db not in DATABASES:
        LOG.debug('opening database %s' % db)
        DATABASES[db] = shelve.open('%s/%s' % (PATH, db), writeback=True)


def db_delete(db):
    LOG.debug('deleting database %s' % db)

    if db in DATABASES:
        DATABASES[db].close()
        DATABASES.pop(db, None)

        os.remove('%s/%s' % (PATH, db))
    else:
        LOG.debug('tried to delete unknown database %s' % db)


def doc_fetch(db, doc):
    LOG.debug('with database %s fetching document %s' % (db, doc))
    db_init(db)
    print(DATABASES[db].get(doc, None))


def doc_init(db, doc):
    LOG.debug('with database %s initializing document %s' % (db, doc))
    db_init(db)
    DATABASES[db][doc] = None
    DATABASES[db].sync()


def doc_save(db, doc, content):
    LOG.debug('with database %s saving document %s' % (db, doc))
    db_init(db)
    DATABASES[db][doc] = content
    DATABASES[db].sync()


def doc_delete(db, doc):
    LOG.debug('with database %s deleting document %s' % (db, doc))
    db_init(db)
    DATABASES[db].pop(doc, None)
    DATABASES[db].sync()
