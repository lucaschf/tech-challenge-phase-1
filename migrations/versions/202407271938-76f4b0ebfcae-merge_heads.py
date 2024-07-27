"""Merge heads

Revision ID: 76f4b0ebfcae
Revises: 1e10e08e89c2, e4134fa90001
Create Date: 2024-07-27 19:38:43.196513

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '76f4b0ebfcae'
down_revision: Union[str, None] = ('1e10e08e89c2', 'e4134fa90001')
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
