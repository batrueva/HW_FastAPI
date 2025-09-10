import pytest
from httpx import AsyncClient, ASGITransport
from app import app
import requests
from bs4 import BeautifulSoup


@pytest.mark.asyncio
async def test_index():
    async with AsyncClient(
            transport=ASGITransport(app=app),
            base_url="http://127.0.0.1",
    ) as ac:
        response = await ac.get("/")
        assert response.status_code == 200
        soup = BeautifulSoup(response.content, "html.parser")
       
        selector_title = "body > h1" 
        assert 'Главная страница' == soup.select_one(selector_title).text
        

@pytest.mark.asyncio
async def test_about():
    async with AsyncClient(
            transport=ASGITransport(app=app),
            base_url="http://127.0.0.1",
    ) as ac:
        response = await ac.get("/about/")
        assert response.status_code == 200    
        soup = BeautifulSoup(response.content, "html.parser")
       
        selector_title = "body > h1" 
        assert 'О нас' == soup.select_one(selector_title).text   