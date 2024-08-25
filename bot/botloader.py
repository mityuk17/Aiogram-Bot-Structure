from aiogram import Bot, Dispatcher, Router
from aiogram.client.default import DefaultBotProperties
from aiogram.fsm.storage.redis import RedisStorage
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.jobstores.sqlalchemy import SQLAlchemyJobStore
from sqlmodel import SQLModel
from apscheduler.jobstores.redis import RedisJobStore
from database.base import DatabaseManager
from config import config


class BotLoader:
    
    def __init__(self, token: str, redis_url: str, postgres_url: str):
        self.tg_bot = Bot(token=token, default=DefaultBotProperties(parse_mode="HTML", link_preview_is_disabled=True))
        self.dispatcher = Dispatcher(storage=RedisStorage.from_url(redis_url))
        RedisJobStore()
        self.scheduler = AsyncIOScheduler(jobstores={"default": SQLAlchemyJobStore(url=postgres_url.replace("+asyncpg", ""), metadata=SQLModel.metadata)})
        self.database_manager = DatabaseManager(postgres_url)
        
    
    def include_routers(self, routers: list[Router]):
        for router in routers:
            self.dispatcher.include_router(router)
    
    
    async def run(self):
        await self.database_manager.init_database()
        self.scheduler.start()
        await self.dispatcher.start_polling(self.tg_bot)
        

bot_loader = BotLoader(token=config.TELEGRAM_BOT_API_TOKEN,
                       redis_url=f"redis://{config.REDIS_USER}:{config.REDIS_PASSWORD}@{config.REDIS_HOST}:{config.REDIS_PORT}",
                       postgres_url=f"postgresql+asyncpg://{config.POSTGRES_USER}:{config.POSTGRES_PASSWORD}@{config.POSTGRES_HOST}:{config.POSTGRES_PORT}/{config.POSTGRES_DB}")