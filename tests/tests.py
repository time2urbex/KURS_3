from utils import get_posts_all, get_comments_all, get_posts_by_user, get_comments_by_post_id, search_for_posts, get_post_by_pk, test_zero
import json
import pytest
#это тест



def test_get_post_by_user_name_type_error(self):
    post = Posts(DATA_PATH)
    with pytest.raises(TypeError):
        post.get_posts_by_user(1)

def test_get_post_by_user_name_type_error(self):
    post = Posts(DATA_PATH)
    with pytest.raises(ValueError):
        post.get_posts_by_user('1')




def test_sum_func(two_numbers_sum):  # обратите внимание на имя

    sum_result = sum_func(two_numbers_sum[0], two_numbers_sum[1])
    assert sum_result == two_numbers_sum[2], "Ошибка для 0 лет"


import pytest

from utils import ticket_price

class TestTicketPrice:

    def test_0(self):
        assert ticket_price(0) == "Бесплатно", "Ошибка для 0 лет"

    def test__1(self):
        assert ticket_price(1) == "Бесплатно", "Ошибка для 1 лет"

    def test_7(self):
        assert ticket_price(7) == "100 рублей", "Ошибка для 7 лет"

    def test_18(self):
        assert ticket_price(18) == "200 рублей", "Ошибка для 18 лет"

    def test_25(self):
        assert ticket_price(25) == "300 рублей", "Ошибка для 25 лет"

    def test_60(self):
        assert ticket_price(60) == "Бесплатно", "Ошибка для 60 лет"

    def test_minus_1(self):
        assert ticket_price(-1) == "Ошибка", "Ошибка для -1 лет"