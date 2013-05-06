import json
import os
import os.path

from cargo.model import Database
from cargo.model import Document


def path(db, doc=None):
    pieces = ['/tmp/cargodb', db, doc]

    if not pieces[-1]:
        pieces.pop()

    return os.path.join(*pieces)


class FlatFileDocument(object):
    def save(self, obj):
        try:
            with open(path(obj.db, obj.doc), 'w') as f:
                f.write(json.dumps(obj.content))
        except IOError:
            return False

        return True

    def load(self, obj):
        with open(path(obj.db, obj.doc), 'r') as f:
            obj.content = json.loads(f.readlines())
        return obj

    def exists(self, obj):
        return os.path.exists(path(obj.db, obj.doc))


class FlatFileDatabase(object):
    def save(self, obj):
        try:
            os.makedirs(path(obj.db))
        except OSError:
            return False

        return True

    def load(self, obj):
        pass

    def delete(self, obj):
        try:
            os.rmdir(path(obj.db))
        except OSError:
            return False

        return True

    def exists(self, obj):
        return os.path.exists(path(obj.db))


class FlatFile(object):
    def __init__(self):
        self.types = {}
        self.types[Database] = FlatFileDatabase()
        self.types[Document] = FlatFileDatabase()

    def by_type(self, obj):
        return self.types[type(obj)]

    def save(self, obj):
        return self.by_type(obj).save(obj)

    def delete(self, obj):
        return self.by_type(obj).delete(obj)

    def load(self, obj):
        return self.by_type(obj).load(obj)

    def exists(self, obj):
        return self.by_type(obj).exists(obj)
