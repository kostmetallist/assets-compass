from datetime import datetime, UTC
from functools import partial

from fastapi_users_db_sqlalchemy import SQLAlchemyBaseUserTable
from sqlalchemy import MetaData, Table, Column, ForeignKey, Integer, String, JSON, TIMESTAMP, Boolean

from src.database import Base, metadata


role = Table(
    'role',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String, nullable=False),
    Column('permissions', JSON)
)


class User(SQLAlchemyBaseUserTable[int], Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    email = Column(String, nullable=False)
    username = Column(String, nullable=False)
    hashed_password = Column(String(length=1024), nullable=False)
    registered_at = Column(TIMESTAMP(timezone=True), default=partial(datetime.now, UTC))
    role_id = Column(Integer, ForeignKey(role.c.id))
    is_active = Column(Boolean, default=True, nullable=False)
    is_superuser = Column(Boolean, default=False, nullable=False)
    is_verified = Column(Boolean, default=False, nullable=False)
