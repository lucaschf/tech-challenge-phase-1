"""order tables.

Revision ID: 350e7d349a60
Revises: a1242ea8396e
Create Date: 2024-05-26 22:09:05.916308

"""

from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision: str = "350e7d349a60"
down_revision: Union[str, None] = "a1242ea8396e"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:  # noqa: D103
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "orders",
        sa.Column("user_uuid", sa.UUID(), nullable=False),
        sa.Column("status", sa.String(), nullable=False),
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("uuid", sa.UUID(), nullable=False),
        sa.Column(
            "created_at",
            sa.DateTime(timezone=True),
            server_default=sa.text("now()"),
            nullable=False,
        ),
        sa.Column(
            "updated_at",
            sa.DateTime(timezone=True),
            server_default=sa.text("now()"),
            nullable=False,
        ),
        sa.ForeignKeyConstraint(["user_uuid"], ["customers.uuid"]),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(op.f("ix_orders_uuid"), "orders", ["uuid"], unique=True)
    op.create_table(
        "order_products",
        sa.Column("order_uuid", sa.UUID(), nullable=False),
        sa.Column("product_uuid", sa.UUID(), nullable=False),
        sa.Column("quantity", sa.Integer(), nullable=False),
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("uuid", sa.UUID(), nullable=False),
        sa.Column(
            "created_at",
            sa.DateTime(timezone=True),
            server_default=sa.text("now()"),
            nullable=False,
        ),
        sa.Column(
            "updated_at",
            sa.DateTime(timezone=True),
            server_default=sa.text("now()"),
            nullable=False,
        ),
        sa.ForeignKeyConstraint(["order_uuid"], ["orders.uuid"]),
        sa.ForeignKeyConstraint(["product_uuid"], ["products.uuid"]),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(op.f("ix_order_products_uuid"), "order_products", ["uuid"], unique=True)
    # ### end Alembic commands ###


def downgrade() -> None:  # noqa: D103
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f("ix_order_products_uuid"), table_name="order_products")
    op.drop_table("order_products")
    op.drop_index(op.f("ix_orders_uuid"), table_name="orders")
    op.drop_table("orders")
    # ### end Alembic commands ###
