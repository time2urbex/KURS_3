# Прежде, чем приступать к написанию Flask-приложения, полезно разработать функции, для работы с данными и сложить их в отдельном файле, например, `utils.py.` Например:

# `get_posts_all()` – возвращает посты

import json


# Загружаем посты из json


def get_posts_all() -> list[dict]:
    with open('./data/posts.json', r, encoding='utf-8') as posts_file:
        return json.load(posts_file)


def get_comments_all() -> list[dict]:
    with open('./data/comments.json', r, encoding='utf-8') as comments_file:
        return json.load(comments_file)


# `get_posts_by_user(user_name)` – возвращает посты определенного пользователя. Функция должна вызывать

def get_posts_by_user(user_name: str) -> list[dict]:
    posts_result = []
    for post in get_posts_all():
        if user_name.lower() in post['poster_name'].lower():
            posts_result.append(post)
    return posts_result


# ошибку `ValueError` если такого пользователя нет и пустой список, если у пользователя нет постов.
# `get_comments_by_post_id(post_id)` – возвращает комментарии определенного поста. Функция должна вызывать
# ошибку `ValueError` если такого поста нет и пустой список, если у поста нет комментов.

def get_comments_by_post_id(post_id: str) -> list[dict]:
    comments_result = []
    for comments in get_comments_all():
        if post_id.lower() in post['post_id'].lower():
            comments_result.append(comments)
    return comments_result


# `search_for_posts(query)` – возвращает список постов по ключевому слову

def search_for_posts(query: str) -> list[dict]:
    search_result = []
    for posts in get_posts_all():
        if query.lower() in posts['content'].lower():
            search_result.append(posts)
    return search_result


# `get_post_by_pk(pk)` – возвращает один пост по его идентификатору.

def get_post_by_pk(pk: str) -> list[dict]:
    id_search_result = []
    for posts in get_posts_all():
        if pk.lower() in posts['pk'].lower():
            id_search_result.append(posts)
    return id_search_result


def test_zero():
    assert get_post_by_pk(1) == 1, "Неверно для 1"

# Напишите к каждой функции юнит тесты, расположите тесты в отдельной папке `/tests`.

# Организуйте тесты в виде классов или функций, на ваше усмотрение.
