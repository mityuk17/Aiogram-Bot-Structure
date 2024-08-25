from aiogram import BaseMiddleware
from database.crud.user import get_user, update_user, create_user
from schemas import User
from datetime import datetime


class UserUpdateOrCreateMiddleware(BaseMiddleware):
    async def __call__(self, handler, event, data):
        try:
            tg_user = event.from_user
            user = await get_user(tg_user.id)
            
            if user:
                user.username = tg_user.username
                user.name = tg_user.full_name
                user.last_activity = datetime.now()
                await update_user(user)
            else:
                new_user = User(id=tg_user.id, username=tg_user.username, name=tg_user.full_name)
                await create_user(new_user)
                
        except AttributeError:
            pass
            
        return await handler(event, data)
    
                