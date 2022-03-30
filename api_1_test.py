import pytest

from api_1 import app

def test_app_poster_name_1():
    response = app.test_client().get('/api/posts/1')
    assert response.json.get("poster_name") == "leo", "Отсутствует ключ poster_name"

def test_app_views_count_1():
        response = app.test_client().get('/api/posts/1')
        assert response.json.get("views_count") == 376, "Отсутствует ключ views_count"

def test_app_likes_count_1():
    response = app.test_client().get('/api/posts/1')
    assert response.json.get("likes_count") == 154, "Отсутствует ключ likes_count"

def test_app_pk_1():
    response = app.test_client().get('/api/posts/1')
    assert response.json.get("pk") != None, "Отсутствует ключ pk"

def test_app_pic_1():
    response = app.test_client().get('/api/posts/1')
    assert response.json.get("pic") != None, "Отсутствует ключ pic"

def test_app_content_1():
    response = app.test_client().get('/api/posts/4')
    assert response.json.get("content") != None, "Отсутствует ключ content"


def test_app_poster_name_4():
    response = app.test_client().get('/api/posts/4')
    assert response.json.get("poster_name") == "larry", "Отсутствует ключ poster_name"

def test_app_views_count_4():
        response = app.test_client().get('/api/posts/4')
        assert response.json.get("views_count") == 366, "Отсутствует ключ views_count"

def test_app_likes_count_4():
    response = app.test_client().get('/api/posts/4')
    assert response.json.get("likes_count") == 198, "Отсутствует ключ likes_count"

def test_app_pk_4():
    response = app.test_client().get('/api/posts/4')
    assert response.json.get("pk") != None, "Отсутствует ключ pk"

def test_app_pic_4():
    response = app.test_client().get('/api/posts/4')
    assert response.json.get("pic") != None, "Отсутствует ключ pic"

def test_app_content_4():
    response = app.test_client().get('/api/posts/4')
    assert response.json.get("content") != None, "Отсутствует ключ content"

