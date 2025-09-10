from fastapi import APIRouter, FastAPI, HTTPException, Query, Request
from models.books import Book
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.templating import Jinja2Templates

router = APIRouter()
templates = Jinja2Templates(directory="templates")
book_list = [
    Book(title="Миссия выполнима", year=2025, description="Технология счастливой жизни", img="Book_1.jpg", autor = "Мургулан Сейсембай"),
    Book(title="Антихрупкость", year=2012, description="Как извлечь выгоду из хаоса", img="Book_2.jpg", autor = "Нассим Николас Талеб"),
    Book(title="Черный лебедь", year=2007, description="Под знаком непредсказуемости", img="Book_3.jpg", autor = "Нассим Николас Талеб"),
    Book(title="Одураченные случайностью", year=2004, description="О скрытой роли шанса в бизнесе и жизни", img="Book_4.jpg", autor = "Нассим Николас Талеб"),
    Book(title="Рискуя собственной шкурой", year=2014, description="Скрытая ассиметрия повседневной жизни", img="Book_5.jpg", autor = "Нассим Николас Талеб")
]



@router.get("/books/", response_class=HTMLResponse)
async  def get_books(
    request: Request,
    year: int = Query(None, description="Год выпука книги"),
    title: str = Query(None, description="Наименование книги"),
    autor: str = Query(None, description="Автор книги")
):
    """получить список книг"""
    result = book_list
    if year is not None:
        result = [book for book in result if book.year == year]
    if title is not None:
        result = [book for book in result if book.title == title]
    if autor is not None:
        result = [book for book in result if book.autor == autor]
    title = "Книжная полка"
    text = "Книжная полка"
    context = {"request": request,
               "title": title,
               "text": text,
               "books": result}
    return templates.TemplateResponse("books.html", context=context)    



@router.get("/books/{book_id}", response_model=Book)
async def get_book_by_id(book_id: int):
    """получить информацию о книге"""
    if book_id < 0 or book_id >= len(book_list):
        raise HTTPException(status_code=404, detail="Такая книга не найдена")
    else:
        return book_list[book_id]


@router.post("/books/", status_code=201)
async def create_book(book: Book):
    """добавить новую книгу."""
    for m in book_list:
        if m.title == book.title and m.year == book.year:
            raise HTTPException(status_code=409, detail="Такая книга уже есть в библиотеке")
    book_list.append(book)
    return JSONResponse(
        status_code=201,
        content={"message": "Книга добавлена"},
    )
    


@router.put("/books/{book_id}")
async def edit_book(book_id: int, book: Book):
    """изменить описание книги."""
    if book_id < 0 or book_id >= len(book_list):
        raise HTTPException(status_code=404, detail="Такая книга не найдена")
    book_list[book_id] = book
    return JSONResponse(
        status_code=201,
        content={"message": "Книга отредактирована"},
    )
   


@router.delete("/books/{book_id}")
async def delete_book(book_id: int):
    """удалить книгу."""
    if book_id < 0 or book_id >= len(book_list):
        raise HTTPException(status_code=404, detail="Такая книга не найдена")
    return JSONResponse(
        status_code=200,
        content={"message": "Книга удалена"},
    )
   
