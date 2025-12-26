from fastapi import APIRouter
from fastapi import FastAPI, Header, status
from fastapi.exceptions import HTTPException
from typing import Optional, List
from src.books.schemas import BookRequest, BookResponse
from src.books.book_data import books

book_router = APIRouter()



@book_router.get("/", response_model=List[BookResponse])
def get_all_books():
    
    
    return books    




@book_router.post("/", response_model=List[BookResponse])

async def create_book(book_data:BookRequest):

    new_books = {
        "id": 1,
        "name": book_data.name,
        "author": book_data.author,
        "price": book_data.price
    }
    books.append(new_books)
    


    return books


@book_router.get("/{id}")

def get_single_book(id: int):
    for book in books:
        if book["id"] == id:
            return book

    return "books not found"    


@book_router.delete("/{id}")

def delete_book(id: int):
    for book in books:
        if book["id"] == id:
            books.remove(book)
            return "book deleted succesfully"        
    return "book not found"