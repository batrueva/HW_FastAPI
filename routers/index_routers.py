from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

router = APIRouter()
templates = Jinja2Templates(directory="templates")


@router.get("/", response_class=HTMLResponse)
def index(request: Request):
    """"""
    title = 'Главная страница'
    text = "Онлайн библиотека"
    context = {"request": request,
               "title": title,
               "text": text}
    return templates.TemplateResponse("index.html", context=context)

@router.get("/books", response_class=HTMLResponse)
def index(request: Request):
    """"""
    title = 'Книжная полка'
    text = "Книжная полка"
    context = {"request": request,
               "title": title,
               "text": text}
    return templates.TemplateResponse("index.html", context=context)

@router.get("/about/", response_class=HTMLResponse)
def about(request: Request):
    """"""
    title = 'О нас'
    text = "Читайте с удовольствием!"
    context = {"request": request,
               "title": title,
               "text": text}
    return templates.TemplateResponse("about.html", context=context)
