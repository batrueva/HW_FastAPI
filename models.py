from pydantic import BaseModel


class Book(BaseModel):
    title: str
    year: int
    description: str
    img: str
    autor: str
