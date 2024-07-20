"""Add payment table.

Revision ID: 1e10e08e89c2
Revises: ef950d606aa3
Create Date: 2024-07-20 15:21:17.795613

"""

from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision: str = "1e10e08e89c2"
down_revision: Union[str, None] = "ef950d606aa3"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:  # noqa: D103
    op.create_table(
        "payments",
        sa.Column("order_id", sa.Integer(), nullable=True),
        sa.Column(
            "status",
            sa.Enum(
                "PENDING", "PROCESSING", "APPROVED", "REJECTED", "FAILED", name="payment_status"
            ),
            nullable=False,
        ),
        sa.Column("details", sa.JSON(), nullable=True),
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
        sa.ForeignKeyConstraint(["order_id"], ["orders.id"]),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(op.f("ix_payments_uuid"), "payments", ["uuid"], unique=True)


def downgrade() -> None:  # noqa: D103
    op.drop_index(op.f("ix_payments_uuid"), table_name="payments")
    op.drop_table("payments")
