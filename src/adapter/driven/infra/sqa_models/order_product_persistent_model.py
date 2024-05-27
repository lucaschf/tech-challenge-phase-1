from sqlalchemy import Column, ForeignKey, Integer
from sqlalchemy.orm import relationship

from src.core.domain.entities.order_product import OrderProduct as OrderProductEntity

from ..sqa_models.persistent_model import PersistentModel


class OrderProductPersistentModel(PersistentModel):
    """SQLAlchemy model for persisting OrderProduct entities."""

    __tablename__ = "order_products"

    order_uuid = Column(ForeignKey("orders.uuid"), nullable=False)
    product_uuid = Column(ForeignKey("products.uuid"), nullable=False)
    quantity = Column(Integer, nullable=False)
    order = relationship("OrderPersistentModel", back_populates="products")

    def to_entity(self) -> OrderProductEntity:
        """Converts the persistent model to an OrderProduct entity."""
        return OrderProductEntity(
            product_uuid=self.product_uuid,
            quantity=self.quantity,
        )
