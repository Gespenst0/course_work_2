from flask import Flask, Blueprint, jsonify
from utils import load_info_from_json, all_posts

api_blueprint = Blueprint('api_blueprint', __name__)


@api_blueprint.route("/api/posts/<int:pk>")
def get_all_posts(pk):
    posts = load_info_from_json()
    for post in posts:
        if post["pk"] == pk:
            showed_post = post
            break
    return jsonify(showed_post)


@api_blueprint.route("/api/posts")
def get_json_all_posts():
    data = all_posts()
    return jsonify(data)