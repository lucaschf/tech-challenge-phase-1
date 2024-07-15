from sqlalchemy import Column, Float, ForeignKey, Integer
from sqlalchemy.orm import relationship

from src.core.domain.entities.order_item import OrderItem

from .persistent_model import PersistentModel


class OrderItemPersistentModel(PersistentModel):
    """SQLAlchemy model for persisting OrderItem entities."""

    __tablename__ = "order_items"

    order_id = Column(ForeignKey("orders.id"), nullable=False)
    product_id = Column(ForeignKey("products.id"), nullable=False)
    product = relationship("ProductPersistentModel")
    quantity = Column(Integer, nullable=False)
    unit_price = Column(Float, nullable=False)
    order = relationship("OrderPersistentModel", back_populates="items")

    def to_entity(self) -> OrderItem:
        """Converts the persistent model to an OrderItem entity."""
        return OrderItem(
            _id=self.id,
            uuid=self.uuid,
            product=self.product.to_entity(),
            quantity=self.quantity,
            unit_price=self.unit_price,
            created_at=self.created_at,
            updated_at=self.updated_at,
        )

    @staticmethod
    def from_entity(entity: OrderItem, order_id: int) -> "OrderItemPersistentModel":
        """Converts an OrderItem entity to the persistent model."""
        return OrderItemPersistentModel(
            order_id=order_id,
            uuid=entity.uuid,
            created_at=entity.created_at,
            updated_at=entity.updated_at,
            product_id=entity.product.id,
            quantity=entity.quantity,
            unit_price=entity.unit_price,
        )


__all__ = ["OrderItemPersistentModel"]
