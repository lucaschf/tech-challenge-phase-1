"""Use enumeration for product category.

Revision ID: 14ff6315964a
Revises: 350e7d349a60
Create Date: 2024-07-12 12:14:07.692533

"""

from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision: str = "14ff6315964a"
down_revision: Union[str, None] = "350e7d349a60"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:  # noqa: D103
    category_enum = sa.Enum("LANCHE", "ACOMPANHAMENTO", "BEBIDA", "SOBREMESA", name="category")
    category_enum.create(op.get_bind(), checkfirst=True)

    op.execute("ALTER TABLE products ALTER COLUMN category TYPE category USING category::category;")


def downgrade() -> None:  # noqa: D103
    op.alter_column(
        "products",
        "category",
        existing_type=sa.Enum("LANCHE", "ACOMPANHAMENTO", "BEBIDA", "SOBREMESA", name="category"),
        type_=sa.VARCHAR(length=100),
        existing_nullable=False,
    )
    sa.Enum(name="category").drop(op.get_bind(), checkfirst=True)
