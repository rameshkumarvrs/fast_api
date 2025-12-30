
from sqlmodel.ext.asyncio.session import AsyncSession

from .schemas import BookCreateModel, BookUpdateModel
from sqlmodel import select, desc
from .models import BookResponse


class BookService:
    async def get_all_books(self, session:AsyncSession):
        statement = select(BookResponse).order_by(desc(BookResponse.created_at))

        #result = await session.exec(statement)

        pass


    async def get_book(self, book_uid:str, session:AsyncSession):
        pass


    async def create_book(self, book_data:BookCreateModel, session:AsyncSession):
        pass


    async def book_update(self, book_uid:str, update_book_date:BookUpdateModel, session:AsyncSession):
        pass

    async def get_all_books(self, session:AsyncSession):
        pass
        
