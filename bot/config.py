from pydantic_settings import BaseSettings
import os

class BotConfig(BaseSettings):
    TELEGRAM_BOT_API_TOKEN: str
    TELEGRAM_BOT_USERNAME: str

    POSTGRES_HOST: str
    POSTGRES_PORT: int
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_DB: str
    
    REDIS_HOST: str
    REDIS_USER: str
    REDIS_PASSWORD: str
    REDIS_USER_PASSWORD: str
    REDIS_PORT: int
    
    class Config:
        if os.path.exists(".env"):
            env_file = ".env"
            
        #for import in alembic
        elif os.path.exists("../.env"):
            env_file = "../.env"


config = BotConfig()