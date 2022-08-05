
import logging
import json
from flask import Blueprint, render_template, request
from utils import get_posts_all, get_comments_all, get_posts_by_user, get_comments_by_post_id, search_for_posts, get_post_by_pk, test_zero



main_blueprint = Blueprint('main_blueprint', __name__, template_folder='templates')

# Создаем роут главной страницы

@main_blueprint.route('/')
def main_page():
    return render_template('index.html')

# Создаем роут страницы для поиска
"""
@main_blueprint.route('/posts/<postid>')
    get_post_by_pk(<postid>)

 ### Шаг 2 – реализуйте просмотр поста
Создайте представление для одного поста 
`GET /posts/<postid>` 
Получите комментарии из файла `comments.json`, у которых соответствующий `postid`.
Выведите комментарии к посту.
Не обрабатывайте теги – вы сделаете это в одном из следующих шагов. """

@main_blueprint.route('/search/')
    def search_page():
        search_query = request.args.get('s', '')
        logging.info('Выполняю поиск')

        # Делаем проверку на наличие и работоспособность файла

        try:
            posts = search_for_posts(search_query)

        except FileNotFoundError:
            return 'Файл не найден'

        except JSONDecoderError:
            return 'Невалидный файл'
        return render_template('/templates/search.html', query=search_query, posts=posts)


@main_blueprint.route('/users/<username>')
    for posts in get_posts_all():
        if username.lower() in posts['pk'].lower():
            def get_posts_by_user()


"""

def search_page():
    search_query = request.args.get('s', '')
    logging.info('Выполняю поиск')

    # Делаем проверку на наличие и работоспособность файла

    try:
        posts = get_posts_by_word(search_query)

    except FileNotFoundError:
        return 'Файл не найден'

    except JSONDecoderError:
        return 'Невалидный файл'
    return render_template('post_list.html', query=search_query, posts=posts)



import pytest
### Шаг 2 – реализуйте просмотр поста
# создаем фикстуру для тестирования всех вьюшек (main, candidates, vacancies)
@pytest.fixture()
def test_client():
    app = run.app
    return app.test_client()

#Создайте представление для одного поста

#`GET /posts/<postid>`

#Получите комментарии из файла `comments.json`, у которых соответствующий `postid`.

#Выведите комментарии к посту.

#Не обрабатывайте теги – вы сделаете это в одном из следующих шагов.

"""