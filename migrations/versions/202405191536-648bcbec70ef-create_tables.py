"""Create initial tables.

Revision ID: 648bcbec70ef
Revises:#
Create Date: 2024-05-19 15:36:58.142552

"""

from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision: str = "648bcbec70ef"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:  # noqa: D103
    op.create_table(
        "customers",
        sa.Column("name", sa.String(), nullable=True),
        sa.Column("cpf", sa.String(length=11), nullable=True),
        sa.Column("email", sa.String(length=120), nullable=True),
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("uuid", sa.UUID(), nullable=True),
        sa.Column(
            "created_at", sa.DateTime(timezone=True), server_default=sa.text("now()"), nullable=True
        ),
        sa.Column(
            "updated_at", sa.DateTime(timezone=True), server_default=sa.text("now()"), nullable=True
        ),
        sa.CheckConstraint("char_length(cpf) = 11", name="cons_cpf_length"),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("cpf"),
        sa.UniqueConstraint("email"),
    )
    op.create_index(op.f("ix_customers_uuid"), "customers", ["uuid"], unique=True)


def downgrade() -> None:  # noqa: D103
    op.drop_index(op.f("ix_customers_uuid"), table_name="customers")
    op.drop_table("customers")
