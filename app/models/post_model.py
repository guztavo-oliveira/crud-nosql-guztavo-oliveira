from email.policy import HTTP
from http import HTTPStatus
import pymongo
import itertools

from datetime import datetime as dt

client = pymongo.MongoClient("mongodb://localhost:27017")

db = client["kenzie"]

if not db.id.find_one():
    db.id.insert_one({"id": 0})


class Post:
    def __init__(self, title: str, author: str, tags: list, content: str):
        self.title = title
        self.author = author
        self.tags = tags
        self.content = content

    @staticmethod
    def get_id():

        db.id.update_one({"id": {"$gte": 0}}, {"$inc": {"id": 1}})

        post_id = db.id.find_one()

        return post_id["id"]

    def new_post(self):
        self.__dict__["created_at"] = dt.utcnow()
        self.__dict__["_id"] = self.get_id()
        db.posts.insert_one(self.__dict__)

        return self.__dict__

    @staticmethod
    def get_all_posts():
        return db.posts.find()

    @staticmethod
    def get_post_by_id(id: int):
        return db.posts.find_one({"_id": id})

    @staticmethod
    def update_post_by_id(payload: dict, id: int):
        data_old = db.posts.find_one({"_id": id})
        if not data_old:
            raise ValueError
        for key, value in payload.items():
            if type(data_old[key]) == list:
                db.posts.update_many({key: data_old[key]}, {"$push": {"tags": value}})
            db.posts.update_many({key: data_old[key]}, {"$set": {key: value}})

        db.posts.update_one({key: value}, {"$set": {"update_at": dt.utcnow()}})

        return db.posts.find_one({"_id": id})

    @staticmethod
    def delete_post_by_id(id: int):
        return db.posts.find_one_and_delete({"_id": id})
