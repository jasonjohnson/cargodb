import binascii
import logging
from SocketServer import TCPServer, StreamRequestHandler, ThreadingMixIn


LOG = logging.getLogger(__name__)


class StorageServerHandler(StreamRequestHandler):
    def handle(self):
        LOG.debug('handling new connection')

        while True:
            LOG.debug('waiting for command')

            command = self.rfile.readline().strip()

            if not command:
                LOG.debug('breaking due to eof')
                break

            LOG.debug('parsing command')

            pieces = command.split()
            length = len(pieces)

            task = {}
            offset = 0

            if length >= 1:
                task['operation'] = pieces[0]
            if length >= 2:
                task['db'] = pieces[1]
            if length >= 3:
                task['doc'] = pieces[2]
            if length >= 4:
                task['content'] = ' '.join(pieces[3:])

            # If a command reached this point without a database id, it's a
            # diagnostic operation. Let it dispatch into the default offset.
            if 'db' in task:
                offset = binascii.crc32(task['db']) % len(self.server.queues)

            LOG.debug('serializing task %s onto queue %d' % (task, offset))

            self.server.queues[offset].put(task)
            self.wfile.write('ok\n')


class StorageServer(ThreadingMixIn, TCPServer):
    allow_reuse_address = True
    daemon_threads = True
    timeout = None
    queues = None
