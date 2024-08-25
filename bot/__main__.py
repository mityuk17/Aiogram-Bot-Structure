from botloader import bot_loader
from routers import routers_list
from middlewares import UserUpdateOrCreateMiddleware
import asyncio
import logging


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    bot_loader.include_routers(routers_list)
    bot_loader.dispatcher.message.middleware(UserUpdateOrCreateMiddleware())
    asyncio.run(bot_loader.run())