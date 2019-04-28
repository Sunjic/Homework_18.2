from utils import get_mongo_db


class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    @classmethod
    def get_collection(cls):
        db = get_mongo_db()
        return db[cls.__name__]