# from fastapi import FastAPI, Depends
# from models import Product
# from database import session, engine
# import database_models
# from sqlalchemy.orm import Session
# app = FastAPI()

# database_models.Base.metadata.create_all(bind=engine)






# @app.get("/")
# def greet():
#     return "pachela pudungi"


# #products = [
#  #   Product(id =1, name= "phone", description="budget phone", price= 1000, quantity=4),
#   #  Product(id =2, name= "phone", description="budget phone", price= 1000, quantity=4)
# #]


# def get_db():
#     db = session()
#     try:
#         yield db
#     finally:    
#         db.close()

# def init_db():
#     db = session()
#     count = db.query(database_models.Product).count
#     if count == 0:
#         for product in products:
#             db.add(database_models.Product(**product.model_dump()))
#         db.commit()    

# init_db()

# @app.get("/products")
# def get_all_products(db: Session = Depends(get_db)):
#     #db = session()
#     #db.query()
#     db_products = db.query(database_models.Product).all()
#     return db_products


# @app.get("/product/{id}")
# def get_product_by_id(id: int, db: Session = Depends(get_db)):
#     db_product = db.query(database_models.Product).filter(database_models.Product.id == id).first()
#     if db_product:
#         return db_product
        
#     return "product not found"    


# @app.post("/product")
# def add_product(product: Product, db: Session = Depends(get_db)):
#     db.add(database_models.Product(**product.model_dump()))
#     db.commit()
#     return product


# @app.put("/product")
# def update_product(id: int, product: Product):
#     for i in range(len(products)):
#         if products[i].id == id:
#             products[i] = product
#             return "product added successfully"
        
#     return "No products found"    
















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









# @app.get("/")
# async def get_route():
#     return {"message": "welcome to the pagedaaaa boy"}


# @app.get("/greet")

# async def greet(name:str = "Userrrr", age:Optional[int] = 10) -> dict:
#     return {"message": f"welcome to the {name}", "age": age}


# class BookCreateModel(BaseModel):
#     title : str
#     author : str


#@app.post("/create_book")
#async def create_book(book_data:BookCreateModel):
 #   return {
  #      "title": book_data.title,
   #     "author": book_data.author
   # }

# @app.get('/get_headers', status_code=300)

# async def get_headers(
#     accept:str = Header(None),
#     content_type:str = Header(None),
#     user_agent:str = Header(None)

# ):
    
#     request_headers = {}

#     request_headers["Accept"] = accept
#     request_headers["Content-Type"] = content_type
#     request_headers["User-Agent"] = user_agent

#     return request_headers    


    





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
    


   





























