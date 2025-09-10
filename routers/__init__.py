from fastapi import APIRouter
from .book_router import router as book_router
from .index_routers import router as index_router

app_router = APIRouter()
app_router.include_router(index_router)
app_router.include_router(book_router)

