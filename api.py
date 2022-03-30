from flask import Flask, render_template, request, jsonify

from utils import all_posts

app = Flask(__name__)


@app.route("/api/posts")
def get_json_all_posts():
    data = all_posts()[0]
    return jsonify(data)


if __name__ == "__main__":
  app.run()