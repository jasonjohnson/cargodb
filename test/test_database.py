from requests import delete, get, put
import unittest


def path(db):
    return "http://127.0.0.1:8080/%s" % db


class TestDatabaseOperations(unittest.TestCase):
    def test_get(self):
        db = "test_get_db"

        put(path(db))
        response = get(path(db))
        delete(path(db))

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['status'], 'OK')

    def test_put(self):
        db = "test_put_db"

        response = put(path(db))
        delete(path(db))

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['status'], 'Created')

    def test_delete(self):
        db = "test_delete_db"

        put(path(db))
        response = delete(path(db))

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['status'], 'Deleted')
