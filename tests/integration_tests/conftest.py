import pytest
from models.books import Book


@pytest.fixture
def test_book1():
    return {"title":"Миссия выполнима", "year":2025, "description":"Технология счастливой жизни", "img":"Book_1.jpg", "autor" : "Мургулан Сейсембай"}

@pytest.fixture
def test_book2():
    return {"title":"Миссия выполнима1", "year":2026, "description":"Технология счастливой жизни1", "img":"Book_1.jpg", "autor" : "Мургулан Сейсембай"}

@pytest.fixture
def test_book3():
    return {"title":"Миссия выполнима3", "year":2027, "description":"Технология счастливой жизни3", "img":"Book_1.jpg", "autor" : "Мургулан Сейсембай"}