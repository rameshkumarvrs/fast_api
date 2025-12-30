from sqlmodel  import create_engine, text, SQLModel 
from sqlalchemy.ext.asyncio import AsyncEngine
from src.config import Config
from src.books.models  import BookResponse


engine = AsyncEngine(
create_engine(
    url=Config.DATABASE_URL,
    echo=True
))


async def init_db():
    async with engine.begin() as conn:
       from src.books.models  import BookResponse 

       await conn.run_sync(SQLModel.metadata.create_all)