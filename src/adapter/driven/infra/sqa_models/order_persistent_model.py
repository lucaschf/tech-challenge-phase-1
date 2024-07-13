from typing import List

from sqlalchemy import Column, ForeignKey, Integer
from sqlalchemy.orm import Mapped, relationship

from src.core.domain.entities import Order as OrderEntity
from src.core.domain.value_objects import OrderStatus

from . import CustomerPersistentModel
from .order_item_persistent_model import OrderItemPersistentModel
from .persistent_model import PersistentModel


class OrderPersistentModel(PersistentModel):
    """SQLAlchemy model for persisting Order entities."""

    __tablename__ = "orders"

    customer_id: Mapped[int] = Column(Integer, ForeignKey("customers.id"))
    customer: Mapped[CustomerPersistentModel] = relationship("CustomerPersistentModel")
    items: Mapped[List[OrderItemPersistentModel]] = relationship(
        "OrderItemPersistentModel", back_populates="order"
    )

    total_value: Mapped[float]
    status: Mapped[OrderStatus]

    def to_entity(self) -> OrderEntity:
        """Converts the persistent model to an Order entity."""
        return OrderEntity(
            _id=self.id,
            _items=[item.to_entity() for item in self.items],
            _total_value=self.total_value,
            _status=self.status,
            customer=self.customer.to_entity(),
            uuid=self.uuid,
            created_at=self.created_at,
            updated_at=self.updated_at,
        )

    @staticmethod
    def from_entity(entity: OrderEntity) -> "OrderPersistentModel":
        """Converts an Order entity to the persistent model."""
        return OrderPersistentModel(
            customer_id=entity.customer.id,
            items=[OrderItemPersistentModel.from_entity(item, entity.id) for item in entity.items],
            total_value=entity.total_value,
            status=entity.status,
            uuid=entity.uuid,
            id=entity.id,
            created_at=entity.created_at,
            updated_at=entity.updated_at,
        )


__all__ = ["OrderPersistentModel"]
