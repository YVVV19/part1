from fastapi import FastAPI, status
from pydantic import BaseModel
from typing import Optional

app=FastAPI()

class Book(BaseModel):
    id: int
    name:str
    author:str
    year:int = None
    number:int

a = [
    Book(id=1,name="cevfb",author="crsdcfv",year=2000,number=10),
    Book(id=2,name="cevfb",author="crsdcfv",year=2000,number=10),
    Book(id=3,name="cevfb",author="crsdcfv",year=2000,number=10),
    Book(id=4,name="cevfb",author="crsdcfv",year=2000,number=10),
    Book(id=5,name="cevfb",author="crsdcfv",year=2000,number=10),
    ]

@app.get("/books/")
async def books():
    return a


@app.post("/books/")
async def create_books(book:Book):
    for book in a:
        if book.id == id:
            return status.HTTP_201_CREATED
        else:
            a.append(book)
    return a


@app.get("/book/{id}", response_model=Book)
async def book_id(id: int):
    for book in a:
        if book.id == id:
            return book, status.HTTP_200_OK
        elif book.id != id:
            return status.HTTP_404_NOT_FOUND