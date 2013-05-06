class Document(object):
    def __init__(self, db, doc=None, content=None):
        self.db = db
        self.doc = doc
        self.content = content
