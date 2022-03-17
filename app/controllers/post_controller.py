from http import HTTPStatus
from flask import jsonify, request
from app.models.post_model import Post


def add_post():

    data = request.get_json()
    try:
        post = Post(**data)
        post.new_post()
    except TypeError as e:
        return {
            "err": "Invalid key. Only acceptable keys: author, title, tags, content"
        }, HTTPStatus.BAD_REQUEST

    return post.__dict__, HTTPStatus.CREATED


def get_all():

    return jsonify(list(Post.get_all_posts())), HTTPStatus.OK


def get_by_id(id: int):
    response = Post.get_post_by_id(id)

    if not response:
        return {"err": f"Not found post with id {id}"}, HTTPStatus.NOT_FOUND

    return response, HTTPStatus.OK


def update_post(id: int):
    data = request.get_json()
    valid_json = ["author", "title", "tags", "content"]

    for key in data.keys():
        if key not in valid_json:
            return {
                "err": "Invalid key. Only acceptable keys: author, title, tags, content"
            }, HTTPStatus.BAD_REQUEST

    try:
        return Post.update_post_by_id(data, id), HTTPStatus.OK
    except ValueError:
        return {"err": f"Not found post with id {id}"}, HTTPStatus.BAD_REQUEST


def delete_post(id: int):
    deleted_post = Post.delete_post_by_id(id)

    if not deleted_post:
        return {"err": "Not found post with id"}, HTTPStatus.NOT_FOUND

    return deleted_post
