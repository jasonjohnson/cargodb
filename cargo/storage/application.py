import logging
from Queue import Queue
from threading import Thread
from cargo.storage.server import StorageServer, StorageServerHandler
from cargo.storage.worker import worker


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
 
    LOG.debug('starting storage server')
    server = StorageServer(('127.0.0.1', 8081), StorageServerHandler)
    server.queues = QUEUES

    try:
        server.serve_forever()
    except KeyboardInterrupt:
        for queue in QUEUES:
            LOG.debug('joining task queue %s' % queue)
            queue.join()
