from sqlalchemy import Column, DateTime, Enum, Integer, String
from sqlalchemy.dialects.postgresql import UUID as SA_UUID
from sqlalchemy.orm import relationship

from src.adapter.driven.infra.config.database import Base
from src.core.domain.entities.order import Order as OrderEntity
from src.core.domain.value_objects.order_status import OrderStatus


class OrderPersistentModel(Base):
    """SQLAlchemy model for persisting Order entities."""

    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True)
    uuid = Column(SA_UUID(as_uuid=True), unique=True, index=True, nullable=False)
    user_id = Column(String, nullable=False)
    status = Column(Enum(OrderStatus), nullable=False)
    created_at = Column(DateTime, nullable=False)
    updated_at = Column(DateTime, nullable=False)
    products = relationship("OrderProductPersistentModel", back_populates="order")

    def to_entity(self) -> OrderEntity:
        """Converts the persistent model to an Order entity."""
        return OrderEntity(
            id=self.id,
            uuid=self.uuid,
            user_id=self.user_id,
            products=[product.to_entity() for product in self.products],
            status=self.status,
            created_at=self.created_at,
            updated_at=self.updated_at,
        )
