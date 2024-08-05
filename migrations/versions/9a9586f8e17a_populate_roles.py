"""Populate roles

Revision ID: 9a9586f8e17a
Revises: e80bf471dae5
Create Date: 2024-08-05 15:13:51.612335

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '9a9586f8e17a'
down_revision: Union[str, None] = 'e80bf471dae5'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None

role_table = sa.sql.table(
    'role',
    sa.column('id', sa.Integer),
    sa.column('name', sa.String),
    sa.column('permissions', sa.JSON)
)


def upgrade() -> None:
    op.bulk_insert(
        role_table,
        [
            {
                'id': 1,
                'name': 'normie',
                'permissions': None
            },
            {
                'id': 2,
                'name': 'admin',
                'permissions': None
            },
        ]
    )


def downgrade() -> None:
    op.execute(f'TRUNCATE TABLE {role_table.name}')
