import logging
from Queue import Queue
from SimpleXMLRPCServer import SimpleXMLRPCServer
from threading import Thread
from cargo.storage.worker import worker
from cargo.storage.operations import (db_fetch, db_init, db_delete, doc_fetch,
                                      doc_save, doc_delete)


logging.basicConfig(level=logging.DEBUG)

LOG = logging.getLogger(__name__)

WORKERS = 4
QUEUES = []
THREADS = []


def main():
    LOG.debug('starting storage task threads')

    for _ in range(WORKERS):
        queue = Queue()

        thread = Thread(target=worker, args=(queue,))
        thread.daemon = True
        thread.start()

        QUEUES.append(queue)        
        THREADS.append(thread)
 
    LOG.debug('starting storage xmlrpc server')

    server = SimpleXMLRPCServer(('127.0.0.1', 8081))
    server.register_function(db_fetch)
    server.register_function(db_init)
    server.register_function(db_delete)
    server.register_function(doc_fetch)
    server.register_function(doc_save)
    server.register_function(doc_delete)
    server.register_introspection_functions()

    try:
        server.serve_forever()
    except KeyboardInterrupt:
        for queue in QUEUES:
            LOG.debug('joining task queue %s' % queue)
            queue.join()
