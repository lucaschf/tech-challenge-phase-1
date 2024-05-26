from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from src.core.domain.entities.order_product import OrderProduct as OrderProductEntity

from ..sqa_models.persistent_model import PersistentModel


class OrderProductPersistentModel(PersistentModel):
    """SQLAlchemy model for persisting OrderProduct entities."""

    __tablename__ = "order_products"

    order_id = Column(ForeignKey("orders.id"), nullable=False)
    product_id = Column(String, nullable=False)
    quantity = Column(Integer, nullable=False)
    order = relationship("OrderPersistentModel", back_populates="products")

    def to_entity(self) -> OrderProductEntity:
        """Converts the persistent model to an OrderProduct entity."""
        return OrderProductEntity(
            id=self.id,
            uuid=self.uuid,
            order_id=self.order_id,
            product_id=self.product_id,
            quantity=self.quantity,
        )
