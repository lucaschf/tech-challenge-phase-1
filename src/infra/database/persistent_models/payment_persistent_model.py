from sqlalchemy import JSON, Column, ForeignKey, Integer
from sqlalchemy.orm import Mapped, relationship

from src.core.domain.entities.payment import Payment, PaymentStatus

from .order_persistent_model import OrderPersistentModel
from .persistent_model import PersistentModel


class PaymentPersistentModel(PersistentModel):
    """SQLAlchemy model for persisting payment entities."""

    __tablename__ = "payments"

    order_id: Mapped[int] = Column(Integer, ForeignKey("orders.id"))
    order: Mapped[OrderPersistentModel] = relationship("OrderPersistentModel")
    status: Mapped[PaymentStatus]
    details: Mapped[dict] = Column(JSON)

    def to_entity(self) -> Payment:
        """Converts the persistent model to an Order entity."""
        return Payment(
            _id=self.id,
            status=self.status,
            uuid=self.uuid,
            created_at=self.created_at,
            updated_at=self.updated_at,
            order=self.order.to_entity(),
            details=self.details,
        )

    @staticmethod
    def from_entity(entity: Payment) -> "PaymentPersistentModel":
        """Converts an Order entity to the persistent model."""
        return PaymentPersistentModel(
            id=entity.id,
            order_id=entity.order.id,
            status=entity.status,
            uuid=entity.uuid,
            details=entity.details,
            created_at=entity.created_at,
            updated_at=entity.updated_at,
        )


__all__ = ["PaymentPersistentModel"]
