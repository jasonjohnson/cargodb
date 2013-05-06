from cargo.model import Document
from cargo.store import FlatFile
from cargo.wsgi.util import ok, error, not_found


driver = FlatFile()


class DocumentController(object):
    def GET(self, db, doc):
        document = Document(db, doc)

        if not driver.exists(document):
            return not_found()

        return ok(driver.load(document))

    def PUT(self, db, doc, content):
        document = Document(db, doc, content)

        if not driver.exists(document):
            return ok(driver.save(document))

        return error({'status': 'Error'})

    def DELETE(self, db, doc):
        pass
