from botloader import bot_loader
from schemas import User
from sqlmodel import select
from datetime import datetime


async def create_user(user_data: User) -> User:
    session = await bot_loader.database_manager.get_session()
    
    session.add(user_data)
    await session.commit()
    await session.refresh(user_data)
    await session.close()
    
    return user_data


async def get_user(user_id: int) -> User | None:
    session = await bot_loader.database_manager.get_session()
    
    statement = select(User).where(User.id == user_id)
    result = await session.exec(statement)
    user = result.one_or_none()
    await session.close()
    
    return user


async def update_user(user_data: User) -> User:
    session = await bot_loader.database_manager.get_session()
    
    session.add(user_data)
    await session.commit()
    await session.close()
    
    return user_data
