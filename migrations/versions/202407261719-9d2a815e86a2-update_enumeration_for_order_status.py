"""update_enumeration_for_order_status.

Revision ID: 9d2a815e86a2
Revises: ef950d606aa3
Create Date: 2024-07-26 17:19:30.383979

"""

from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision: str = "9d2a815e86a2"
down_revision: Union[str, None] = "ef950d606aa3"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Perform the upgrade migration."""
    order_status_enum = sa.Enum(
        "PAYMENT_PENDING",
        "PROCESSING",
        "READY",
        "RECEIVED",
        "COMPLETED",
        "CANCELED",
        name="order_status",
    )
    order_status_enum.create(op.get_bind(), checkfirst=True)

    # Update existing data to match the enum cases
    op.execute("ALTER TYPE order_status ADD VALUE IF NOT EXISTS 'PAYMENT_PENDING';")
    op.execute("ALTER TYPE order_status ADD VALUE IF NOT EXISTS 'RECEIVED';")
    op.execute("ALTER TYPE order_status ADD VALUE IF NOT EXISTS 'PROCESSING';")
    op.execute("ALTER TYPE order_status ADD VALUE IF NOT EXISTS 'READY';")


def downgrade() -> None:
    """Revert the upgrade migration."""
    op.alter_column(
        "orders",
        "status",
        existing_type=sa.Enum(
            "PAYMENT_PENDING",
            "PROCESSING",
            "READY",
            "RECEIVED",
            "COMPLETED",
            "CANCELED",
            name="order_status",
        ),
        type_=sa.VARCHAR(),
        existing_nullable=False,
    )
