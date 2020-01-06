from pymongo import *


class MongoOperations:
    def __init__(self):
        conn = MongoClient("localhost", 27017)
        self.collection = conn.testDB.emp_collection
        self.info = None

    def fetch_data_from_db(self, username, password, ret=False):
        self.info = self.collection.find_one({"username": username})
#        print(username, password)
#        print(self.info)
        if self.info is None:
            return False
        if ret:
            if username == self.info["username"]:
                # print("user already exists")
                return True
        if password == self.info["Password"]:
            return True
        else:
            return False

    def dump_data_to_db(self, username, password, email):
        if not self.fetch_data_from_db(username, password, True):
            self.collection.insert_one({"username": username, "Password": password, "email": email})
            return True
        else:
            return False

    def update_data_in_db(self, username, password):
        if self.fetch_data_from_db(username, password, True):
            self.info["Password"] = password
            self.collection.save(self.info)
            return True
        else:
            return False
