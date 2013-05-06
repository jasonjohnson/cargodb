from cargo.model import Database
from cargo.store import FlatFile
from cargo.wsgi.util import ok, error, not_found


driver = FlatFile()


class DatabaseController(object):
    def GET(self, db):
        database = Database(db)

        if not driver.exists(database):
            return not_found()

        return ok({'status': 'OK'})

    def PUT(self, db):
        database = Database(db)

        if not driver.exists(database):
            if driver.save(database):
                return ok({'status': 'Created'})

        return error({'status': 'Error'})

    def DELETE(self, db):
        database = Database(db)

        if driver.exists(database):
            if driver.delete(database):
                return ok({'status': 'Deleted'})

        return error({'status': 'Error'})
