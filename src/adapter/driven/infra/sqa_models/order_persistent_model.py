from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

from src.core.domain.entities.order import Order as OrderEntity

from ..sqa_models.persistent_model import PersistentModel


class OrderPersistentModel(PersistentModel):
    """SQLAlchemy model for persisting Order entities."""

    __tablename__ = "orders"

    user_id = Column(String, nullable=False)
    status = Column(String, nullable=False)
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
