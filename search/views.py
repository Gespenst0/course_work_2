from flask import Flask, render_template, request, Blueprint
from utils import search_for_posts

search_blueprint = Blueprint('search_blueprint', __name__)


@search_blueprint.route('/search/', methods=['GET', "POST"])
def searching_results():
    search_word = request.values.get('s')
    if search_word == None:
        return render_template("search.html")
    info = search_for_posts(search_word)
    return render_template("search.html", searched_posts=info)

