"""Use enumeration for order status.

Revision ID: cf30b4b60e96
Revises: 14ff6315964a
Create Date: 2024-07-12 14:18:29.654690

"""

from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision: str = "cf30b4b60e96"
down_revision: Union[str, None] = "14ff6315964a"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:  # noqa: D103
    order_status_enum = sa.Enum("PENDING", "COMPLETED", "CANCELED", name="order_status")
    order_status_enum.create(op.get_bind(), checkfirst=True)

    # Update existing data to match the enum cases
    op.execute("UPDATE orders SET status = 'PENDING' WHERE status = 'pending';")
    op.execute("UPDATE orders SET status = 'COMPLETED' WHERE status = 'completed';")
    op.execute("UPDATE orders SET status = 'CANCELED' WHERE status = 'canceled';")

    op.execute(
        "ALTER TABLE orders ALTER COLUMN status TYPE order_status USING status::order_status;"
    )


def downgrade() -> None:  # noqa: D103
    op.alter_column(
        "orders",
        "status",
        existing_type=sa.Enum("PENDING", "COMPLETED", "CANCELED", name="order_status"),
        type_=sa.VARCHAR(),
        existing_nullable=False,
    )
