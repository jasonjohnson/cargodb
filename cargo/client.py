import socket


class Client(object):
    def __init__(self, server=('127.0.0.1', 8081)):
        self.server = server
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.buffer = []

    def connect(self):
        self.socket.settimeout(5.0)
        self.socket.connect(self.server)

    def send(self, *args):
        self.socket.sendall('%s\n' % ' '.join(args))

    def recv(self):
        chunks = []

        while True:
            chunk = self.socket.recv(256)
            chunks.append(chunk)
            
            if chunk[-1] == '\n':
                break

        return chunks

if __name__ == '__main__':
    db = 'example-db'
    doc = 'example-doc'

    client = Client()
    client.connect()

    client.send('db-init', db)
    print(client.recv())

    client.send('doc-init', db, doc)
    print(client.recv())

    client.send('doc-save', db, doc, 'hello world')
    print(client.recv())
