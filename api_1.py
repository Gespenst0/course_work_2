from flask import Flask, jsonify

from utils import load_info_from_json

app = Flask(__name__)


@app.route("/api/posts/<int:pk>")
def get_json_all_posts(pk):

    posts = load_info_from_json()
    for post in posts:
        if post["pk"] == pk:
            showed_post = post
            break
    return jsonify(showed_post)


if __name__ == "__main__":
  app.run()