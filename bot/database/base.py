from sqlalchemy.ext.asyncio import create_async_engine
from sqlmodel import SQLModel
from sqlmodel.ext.asyncio.session import AsyncSession
from config import config


class DatabaseManager:
    def __init__(self, DB_URL: str):
        self.engine = create_async_engine(DB_URL, echo=False, future=True)
    
    async def init_database(self):
        async with self.engine.begin() as connection:
            await connection.run_sync(SQLModel.metadata.create_all)
    
    async def get_session(self) -> AsyncSession:
        async with AsyncSession(self.engine, expire_on_commit=False) as async_session:
            return async_session