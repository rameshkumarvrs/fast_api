
from fastapi import FastAPI, Header
from typing import Optional, List
from pydantic import BaseModel

app = FastAPI()

books = [

        {

        "id": 1,
        "name": "5amclub",
        "author": "rameshkumar",
        "price": 150

        },

        {
        "id": 2,
        "name": "Think and grow",
        "author": "rameshkumar",
        "price": 150
        },

        {
        "id": 3,
        "name": "Atomic habits",
        "author": "rameshkumar",
        "price": 150
        },

        {
            "id": 4,
            "name": "richest man in babilone",
            "author": "rameshkumar",
            "price": 150
        },

        {

            "id": 5,
            "name": "5amclub",
            "author": "rameshkumar",
            "price": 150
        },

        {
            "id": 6,
            "name": "5amclub",
            "author": "rameshkumar",
            "price": 150

        }


    ]





class BookResponse(BaseModel):
    id: int
    name: str
    author: str



@app.get("/books", response_model=List[BookResponse])
def get_all_books():
    
    
    return books    


class BookRequest(BaseModel):

    name: str
    author: str  
    price: int 




@app.post("/books", response_model=List[BookResponse])

async def create_book(book_data:BookRequest):

    new_books = {
        "id": 1,
        "name": book_data.name,
        "author": book_data.author,
        "price": book_data.price
    }
    books.append(new_books)
    


    return books


@app.get("/books/{id}")

def get_single_book(id: int):
    for book in books:
        if book["id"] == id:
            return book

    return "books not found"    


@app.delete("/books/{id}")

def delete_book(id: int):
    for book in books:
        if book["id"] == id:
            books.remove(book)
            return "book deleted succesfully"        
    return "book not found"
    


   





























