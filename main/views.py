from flask import Flask, render_template, request, Blueprint
import json
from utils import all_posts, get_posts_by_user, post_by_pk, comment_append

main_blueprint = Blueprint('main_blueprint', __name__)


@main_blueprint.route("/")
def main_page():
    """
    Главная страница
    """
    return render_template("index.html", searched_posts=all_posts())


@main_blueprint.route('/posts/<int:pk>', methods=['GET', "POST"])
def searching_results(pk):
    commenter_name = request.values.get('commenter_name')
    comment_content = request.values.get('comment_content')
    if len(str(comment_content)) == 0 or len(str(commenter_name)) == 0 or comment_content == None:
        return post_by_pk(pk)
    comment_append(pk, commenter_name, comment_content)
    return post_by_pk(pk)


@main_blueprint.route('/users/<username>')
def user_posts(username):
    users_posts = get_posts_by_user(username)
    return render_template("user-feed.html", searched_posts=users_posts)
