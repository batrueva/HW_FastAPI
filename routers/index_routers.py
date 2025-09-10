from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

router = APIRouter()
templates = Jinja2Templates(directory="templates")


@router.get("/", response_class=HTMLResponse)
async def index(request: Request):
    """Главная страница"""
    title = 'Главная страница'
    text = "Онлайн библиотека"
    context = {"request": request,
               "title": title,
               "text": text}
    return templates.TemplateResponse("index.html", context=context)

@router.get("/about/", response_class=HTMLResponse)
async def about(request: Request):
    """О нас"""
    title = 'О нас'
    text = "Читайте с удовольствием!"
    context = {"request": request,
               "title": title,
               "text": text}
    return templates.TemplateResponse("about.html", context=context)
