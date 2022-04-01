import pytest

from app import app


def test_api_posts_pk_blueprint_type():
    response = app.test_client().get('/api/posts/1')
    assert type(response.json) == dict, "Не тот тип данных"


def test_api_posts_pk_poster_name():
    response = app.test_client().get('/api/posts/1')
    assert response.json.get("poster_name"), "Отсутствует ключ poster_name"


def test_api_posts_pk_views_count():
        response = app.test_client().get('/api/posts/1')
        assert response.json.get("views_count"), "Отсутствует ключ views_count"


def test_api_posts_pk_likes_count():
    response = app.test_client().get('/api/posts/1')
    assert response.json.get("likes_count"), "Отсутствует ключ likes_count"


def test_api_posts_pk_pk():
    response = app.test_client().get('/api/posts/1')
    assert response.json.get("pk"), "Отсутствует ключ pk"


def test_api_posts_pk_pic():
    response = app.test_client().get('/api/posts/1')
    assert response.json.get("pic"), "Отсутствует ключ pic"


def test_api_posts_pk_content():
    response = app.test_client().get('/api/posts/1')
    assert response.json.get("content"), "Отсутствует ключ content"




def test_api_posts_blueprint_type():
    response = app.test_client().get('/api/posts')
    assert type(response.json) == list, "Не тот тип данных"


def test_api_posts_poster_name():
    response = app.test_client().get('/api/posts')
    assert response.json[0].get("poster_name"), "Отсутствует ключ poster_name"


def test_api_posts_views_count():
    response = app.test_client().get('/api/posts')
    assert response.json[0].get("views_count"), "Отсутствует ключ views_count"


def test_api_posts_likes_count():
    response = app.test_client().get('/api/posts')
    assert response.json[0].get("likes_count"), "Отсутствует ключ likes_count"


def test_api_posts_pk():
    response = app.test_client().get('/api/posts')
    assert response.json[0].get("pk"), "Отсутствует ключ pk"


def test_api_posts_pic():
    response = app.test_client().get('/api/posts')
    assert response.json[0].get("pic"), "Отсутствует ключ pic"


def test_api_posts_content():
    response = app.test_client().get('/api/posts')
    assert response.json[0].get("content"), "Отсутствует ключ content"
