import json
from flask import render_template


def load_info_from_json():
    """
    Загрузка информации о всех постах из файла data.json
    """
    with open("data.json", "r") as file:
        posts_json = file.read()
        posts = json.loads(posts_json)
        return posts


def load_comments_from_json():
    """
    Загрузка комментариев о всех постах в файле comments.json
    """
    with open("comments.json", "r") as file:
        comments_json = file.read()
        comments = json.loads(comments_json)
        return comments


def comment_append(pk, commenter_name, comment_content):
    """
    Добавляет новый комментарий
    """
    all_comments = load_comments_from_json()
    new_comment = {"post_id": pk, "commenter_name": commenter_name, "comment": comment_content,
                   "pk": len(all_comments) + 1}
    all_comments.append(new_comment)
    with open("comments.json", "w") as file:
        json_all_comments = json.dumps(all_comments)
        file.write(json_all_comments)


def all_posts():
    """
    Вызврощает все посты
    """
    posts = load_info_from_json()
    return posts


def get_posts_by_user(user_name):
    """
    Возвращает посты определенного пользователя
    """
    posts = all_posts()
    users_posts = []
    for post in posts:
        if post["poster_name"] == user_name:
            users_posts.append(post)
    return users_posts

def get_comments_by_post_id(post_id):
    """
    Возвращает список комментариев определенного поста
    """
    comments = load_comments_from_json()
    showed_comments = []
    for comment in comments:
        if comment["post_id"] == post_id:
            showed_comments.append(comment)
    return showed_comments


def search_for_posts(query):
    """
    Возвращает список постов по ключевому слову
    """
    all_posts = load_info_from_json()
    searched_posts = []
    for post in all_posts:
        if query in post["content"]:
            searched_posts.append(post)
    if len(searched_posts) > 10:
        searched_posts = searched_posts[slice(0, 10)]
    return searched_posts

def post_by_pk(pk):
    """
    Возвращает один пост по его идентификатору
    """
    posts = load_info_from_json()
    for post in posts:
        if post["pk"] == pk:
            showed_post = post
            break
    showed_comments = get_comments_by_post_id(pk)
    return render_template("post.html", post=showed_post, tasks=showed_comments)
