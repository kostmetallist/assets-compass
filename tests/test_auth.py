import pytest
from sqlalchemy import insert, select

from src.auth.models import role
from conftest import async_session_maker, client

@pytest.mark.asyncio
async def test_add_role():
    async with async_session_maker() as session:

        stmt = insert(role).values(id=1, name='normie', permissions=None)
        await session.execute(stmt)
        await session.commit()

        query = select(role)
        result = await session.execute(query)
        assert result.all() == [(1, 'normie', None)]


def test_register():
    client.post('/auth/register', json={
        'email': 'test@example.com',
        'password': 'thisissecret',
        'is_active': True,
        'is_superuser': False,
        'is_verified': False,
        'username': 'test',
        'role_id': 1,
    })