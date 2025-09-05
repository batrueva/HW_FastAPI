from fastapi import APIRouter, FastAPI, HTTPException, Query, Request
from models import Book
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

router = APIRouter()
templates = Jinja2Templates(directory="templates")
book_list = [
    Book(title="Миссия выполнима", year=2023, description="Технология счастливой жизни", img="Book_1.jpg", autor = "Мургулан Сейсембай"),
    Book(title="Антихрупкость", year=2012, description="Как извлечь выгоду из хаоса", img="Book_2.jpg", autor = "Нассим Николас Талеб"),
    Book(title="Черный лебедь", year=2007, description="Под знаком непредсказуемости", img="Book_3.jpg", autor = "Нассим Николас Талеб"),
    Book(title="Одураченные случайностью", year=2004, description="О скрытой роли шанса в бизнесе и жизни", img="Book_4.jpg", autor = "Нассим Николас Талеб"),
    Book(title="Рискуя собственной шкурой", year=2014, description="Скрытая ассиметрия повседневной жизни", img="Book_5.jpg", autor = "Нассим Николас Талеб")
]


# @router.get("/books/", response_model=list[Book])
# def get_books(
#     year: int = Query(None, description="The year of books"),
#     title: str = Query(None, description="The title of books")
# ):
#     """"""
#     result = book_list
#     if year is not None:
#         result = [book for book in result if book.year == year]
#     if title is not None:
#         result = [book for book in result if book.title == title]
#     return result

@router.get("/books/", response_class=HTMLResponse)
def get_books(
    request: Request,
    year: int = Query(None, description="The year of books"),
    title: str = Query(None, description="The title of books"),
    autor: str = Query(None, description="The autor of books")
):
    """"""
    result = book_list
    if year is not None:
        result = [book for book in result if book.year == year]
    if title is not None:
        result = [book for book in result if book.title == title]
    if autor is not None:
        result = [book for book in result if book.autor == autor]
    title = 'Книжная полка'
    text = "Книжная полка"
    context = {"request": request,
               "title": title,
               "text": text,
               "books": result}
    return templates.TemplateResponse("books.html", context=context)    



@router.get("/books/{book_id}", response_model=Book)
def get_book_by_id(book_id: int):
    """получить информацию по фильму"""
    if book_id < 0 or book_id >= len(book_list):
        raise HTTPException(status_code=404, detail="Book not found")
    else:
        return book_list[book_id]


@router.post("/books/", response_model=Book, status_code=201)
def create_book(book: Book):
    """добавить новый фильм."""
    for m in book_list:
        if m.title == book.title and m.year == book.year:
            raise HTTPException(status_code=409, detail="Такая книга уже есть в библиотеке")
    book_list.append(book)
    return book


@router.put("/books/{book_id}")
def edit_book(book_id: int, book: Book):
    """добавить новый фильм."""
    if book_id < 0 or book_id >= len(book_list):
        raise HTTPException(status_code=404, detail="Book not found")
    book_list[book_id] = book
    return book_list[book_id]


@router.delete("/books/{book_id}")
def delete_book(book_id: int):
    """добавить новый фильм."""
    if book_id < 0 or book_id >= len(book_list):
        raise HTTPException(status_code=404, detail="Book not found")

    return book_list.pop(book_id)
