import pytest
from httpx import AsyncClient, ASGITransport
from app import app



@pytest.mark.asyncio
async def test_get_books():
    async with AsyncClient(
            transport=ASGITransport(app=app),
            base_url="http://127.0.0.1",
    ) as ac:
        response = await ac.get("/books/")
        assert response.status_code == 200


@pytest.mark.asyncio
async def test_post_books(test_book2):
    async with AsyncClient(
            transport=ASGITransport(app=app),
            base_url="http://127.0.0.1",
    ) as ac:
        response = await ac.post("/books/", json = test_book2)
        
        assert response.status_code == 201
        data = response.json()
        assert data == {"message": "Книга добавлена"}
       
@pytest.mark.asyncio
async def test_post_books_failed(test_book2):
    async with AsyncClient(
            transport=ASGITransport(app=app),
            base_url="http://127.0.0.1",
    ) as ac:
        response = await ac.post("/books/", json = test_book2)
        
        assert response.status_code == 409
        data = response.json()
        assert data == {"detail": "Такая книга уже есть в библиотеке"}

@pytest.mark.asyncio
async def test_get_book_by_id():
    async with AsyncClient(
            transport=ASGITransport(app=app),
            base_url="http://127.0.0.1",
    ) as ac:
  
        response = await ac.get("/books/0")
        assert response.status_code == 200
        response = await ac.get("/books/10")
        assert response.status_code == 404
        data = response.json()
        assert data == {"detail": "Такая книга не найдена"}  


@pytest.mark.asyncio
async def test_edit_book(test_book1):
    async with AsyncClient(
            transport=ASGITransport(app=app),
            base_url="http://127.0.0.1",
    ) as ac:
  
        response = await ac.put("/books/0", json = test_book1)
        assert response.status_code == 201
        data = response.json()
        assert data == {"message": "Книга отредактирована"}         
        response = await ac.put("/books/10", json = test_book1)
        assert response.status_code == 404
        data = response.json()
        assert data == {"detail": "Такая книга не найдена"}  


@pytest.mark.asyncio
async def test_delete_book():
    async with AsyncClient(
            transport=ASGITransport(app=app),
            base_url="http://127.0.0.1",
    ) as ac:
  
        response = await ac.get("/books/0")
        assert response.status_code == 200
        response = await ac.get("/books/10")
        assert response.status_code == 404
        data = response.json()
        assert data == {"detail": "Такая книга не найдена"}  