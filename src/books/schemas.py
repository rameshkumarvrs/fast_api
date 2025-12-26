from pydantic import BaseModel

class BookResponse(BaseModel):
    id: int
    name: str
    author: str



class BookRequest(BaseModel):

    name: str
    author: str  
    price: int     