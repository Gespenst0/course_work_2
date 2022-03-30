import pytest

from api import app

def test_app_poster_name():
    response = app.test_client().get('/api/posts')
    assert response.json.get("poster_name") == "leo", "Отсутствует ключ poster_name"

def test_app_views_count():
        response = app.test_client().get('/api/posts')
        assert response.json.get("views_count") == 376, "Отсутствует ключ views_count"

def test_app_likes_count():
    response = app.test_client().get('/api/posts')
    assert response.json.get("likes_count") == 154, "Отсутствует ключ likes_count"

def test_app_pk():
    response = app.test_client().get('/api/posts')
    assert response.json.get("pk") != None, "Отсутствует ключ pk"

def test_app_pic():
    response = app.test_client().get('/api/posts')
    assert response.json.get("pic") != None, "Отсутствует ключ pic"

def test_app_content():
    response = app.test_client().get('/api/posts')
    assert response.json.get("content") != None, "Отсутствует ключ content"
