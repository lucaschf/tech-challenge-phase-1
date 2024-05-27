from sqlalchemy import Column, ForeignKey, String
from sqlalchemy.orm import relationship

from src.core.domain.entities.order import Order as OrderEntity
from src.core.domain.value_objects.order_status import OrderStatus

from ..sqa_models.persistent_model import PersistentModel


class OrderPersistentModel(PersistentModel):
    """SQLAlchemy model for persisting Order entities."""

    __tablename__ = "orders"

    user_uuid = Column(ForeignKey("customers.uuid"), nullable=False)
    status = Column(String, nullable=False)
    products = relationship("OrderProductPersistentModel", back_populates="order")

    def to_entity(self) -> OrderEntity:
        """Converts the persistent model to an Order entity."""
        return OrderEntity(
            user_uuid=self.user_uuid,
            products=[product.to_entity() for product in self.products],
            status=OrderStatus(self.status),
            created_at=self.created_at,
            updated_at=self.updated_at,
            uuid=self.uuid,
        )

    @staticmethod
    def from_entity(entity: OrderEntity) -> "OrderPersistentModel":
        """Converts an Order entity to the persistent model."""
        return OrderPersistentModel(
            user_uuid=entity.user_uuid,
            status=entity.status.status,  # Converte o status para string
            uuid=entity.uuid,
            created_at=entity.created_at,
            updated_at=entity.updated_at,
        )
