from sqlmodel import SQLModel, Field
from sqlalchemy import Column, BigInteger, ForeignKey
from datetime import datetime


class User(SQLModel, table=True):
    id: int = Field(sa_column=Column(BigInteger(), primary_key=True))
    username: str | None
    name: str | None
    last_activity: datetime = Field(default=datetime.now())
    registered_at: datetime = Field(default=datetime.now())
    