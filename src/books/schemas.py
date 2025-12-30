from pydantic import BaseModel
import uuid
from datetime import datetime

class BookResponse(BaseModel):
    uid: uuid.UUID
    name: str
    author: str
    created_at: datetime
    updated_at: datetime


class BookCreateModel(BaseModel):
    name: str
    author: str  
    price: int  



class BookUpdateModel(BaseModel):

    name: str
    author: str  
    price: int     