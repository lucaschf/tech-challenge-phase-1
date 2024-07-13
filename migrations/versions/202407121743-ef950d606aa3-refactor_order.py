"""Refactor order.

Revision ID: ef950d606aa3
Revises: cf30b4b60e96
Create Date: 2024-07-12 17:43:44.872195

"""

from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op
from sqlalchemy.dialects import postgresql

CURRENT_DATETIME = "now()"

# revision identifiers, used by Alembic.
revision: str = "ef950d606aa3"
down_revision: Union[str, None] = "cf30b4b60e96"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:  # noqa: D103
    op.create_table(
        "order_items",
        sa.Column("order_id", sa.Integer(), nullable=False),
        sa.Column("product_id", sa.Integer(), nullable=False),
        sa.Column("quantity", sa.Integer(), nullable=False),
        sa.Column("unit_price", sa.Float(), nullable=False),
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("uuid", sa.UUID(), nullable=False),
        sa.Column(
            "created_at",
            sa.DateTime(timezone=True),
            server_default=sa.text(CURRENT_DATETIME),
            nullable=False,
        ),
        sa.Column(
            "updated_at",
            sa.DateTime(timezone=True),
            server_default=sa.text(CURRENT_DATETIME),
            nullable=False,
        ),
        sa.ForeignKeyConstraint(["order_id"], ["orders.id"]),
        sa.ForeignKeyConstraint(["product_id"], ["products.id"]),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(op.f("ix_order_items_uuid"), "order_items", ["uuid"], unique=True)
    op.drop_index("ix_order_products_uuid", table_name="order_products")
    op.drop_table("order_products")
    op.add_column("orders", sa.Column("customer_id", sa.Integer(), nullable=True))
    op.add_column("orders", sa.Column("total_value", sa.Float(), nullable=False))
    op.drop_constraint("orders_user_uuid_fkey", "orders", type_="foreignkey")
    op.create_foreign_key(None, "orders", "customers", ["customer_id"], ["id"])
    op.drop_column("orders", "user_uuid")


def downgrade() -> None:  # noqa: D103
    op.add_column("orders", sa.Column("user_uuid", sa.UUID(), autoincrement=False, nullable=False))
    op.drop_constraint(None, "orders", type_="foreignkey")
    op.create_foreign_key("orders_user_uuid_fkey", "orders", "customers", ["user_uuid"], ["uuid"])
    op.drop_column("orders", "total_value")
    op.drop_column("orders", "customer_id")
    op.create_table(
        "order_products",
        sa.Column("order_uuid", sa.UUID(), autoincrement=False, nullable=False),
        sa.Column("product_uuid", sa.UUID(), autoincrement=False, nullable=False),
        sa.Column("quantity", sa.INTEGER(), autoincrement=False, nullable=False),
        sa.Column("id", sa.INTEGER(), autoincrement=True, nullable=False),
        sa.Column("uuid", sa.UUID(), autoincrement=False, nullable=False),
        sa.Column(
            "created_at",
            postgresql.TIMESTAMP(timezone=True),
            server_default=sa.text(CURRENT_DATETIME),
            autoincrement=False,
            nullable=False,
        ),
        sa.Column(
            "updated_at",
            postgresql.TIMESTAMP(timezone=True),
            server_default=sa.text(CURRENT_DATETIME),
            autoincrement=False,
            nullable=False,
        ),
        sa.ForeignKeyConstraint(
            ["order_uuid"], ["orders.uuid"], name="order_products_order_uuid_fkey"
        ),
        sa.ForeignKeyConstraint(
            ["product_uuid"], ["products.uuid"], name="order_products_product_uuid_fkey"
        ),
        sa.PrimaryKeyConstraint("id", name="order_products_pkey"),
    )
    op.create_index("ix_order_products_uuid", "order_products", ["uuid"], unique=True)
    op.drop_index(op.f("ix_order_items_uuid"), table_name="order_items")
    op.drop_table("order_items")
