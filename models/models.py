from datetime import datetime, UTC
from functools import partial

from sqlalchemy import MetaData, Table, Column, ForeignKey, Integer, String, JSON, TIMESTAMP


metadata = MetaData()

role = Table(
    'role',
    metadata,
    Column(
        'id',
        Integer,
        primary_key=True
    ),
    Column(
        'name',
        String,
        nullable=False
    ),
    Column(
        'permissions',
        JSON
    )
)

user = Table(
    'user',
    metadata,
    Column(
        'id',
        Integer,
        primary_key=True
    ),
    Column(
        'email',
        String,
        nullable=False
    ),
    Column(
        'username',
        String,
        nullable=False
    ),
    Column(
        'password',
        String,
        nullable=False
    ),
    Column(
        'registered_at',
        TIMESTAMP,
        default=partial(datetime.now, UTC)
    ),
    Column(
        'role_id',
        Integer,
        ForeignKey('role.id')
    )
)
