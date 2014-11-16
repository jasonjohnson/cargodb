import logging
from cargo.storage.operations import (db_fetch, db_init, db_delete, doc_fetch,
                                      doc_init, doc_save, doc_delete)


LOG = logging.getLogger(__name__)

OPERATIONS = {
    'db-fetch': db_fetch,
    'db-init': db_init,
    'db-delete': db_delete,
    'doc-fetch': doc_fetch,
    'doc-init': doc_init,
    'doc-save': doc_save,
    'doc-delete': doc_delete
}


def unknown(*args):
    LOG.debug('unknown operation called with %s' % args)


def worker(tasks):
    while True:
        task = tasks.get()

        LOG.debug('processing task %s' % task)

        try:
            operation = OPERATIONS.get(task.pop('operation'), unknown)
            operation(**task)
        finally:
            tasks.task_done()
