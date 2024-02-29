import os

from couchdb import Server


class CouchLogger(object):
    def __init__(self, couchdb_url, db_name):
        self.server = Server(couchdb_url)
        self.db = self.server[db_name]

    def log(self, entry):
        self.db.save(entry)

    @staticmethod
    def from_environment():
        couchdb_host = os.environ.get('COUCHDB_HOST', 'localhost')
        couchdb_user = os.environ.get('COUCHDB_USER', 'admin')
        couchdb_password = os.environ.get('COUCHDB_PASSWORD', 'password')
        couchdb_db = os.environ.get('COUCHDB_DB', 'provenance')
        return CouchLogger(f'http://${couchdb_user}:${couchdb_password}@{couchdb_host}:5984', couchdb_db)
