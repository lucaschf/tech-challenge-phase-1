from sqlalchemy import Column, Enum, Float, ForeignKey, Integer
from sqlalchemy.orm import Mapped, relationship

from src.core.domain.entities.enums import OrderStatus, PaymentMethod

from .persistent_model import PersistentModel


class OrderItemPersistentModel(PersistentModel):
    """This class represents a customer table in the system."""

    __tablename__ = "order_items"

    order_id: Mapped[int] = Column(Integer, ForeignKey("orders.id"))
    product_id: Mapped[int] = Column(Integer, ForeignKey("products.id"), nullable=False, index=True)

    quantity: Mapped[int] = Column(Integer, nullable=False)
    price: Mapped[float] = Column(Float, nullable=False)

    order = relationship("OrderPersistentModel", back_populates="items")
    product = relationship("ProductPersistentModel")


class OrderPersistentModel(PersistentModel):
    """This class represents a customer table in the system."""

    __tablename__ = "orders"

    customer_id: Mapped[int] = Column(Integer, ForeignKey("customers.id"))
    status: Mapped[OrderStatus] = Column(
        Enum(OrderStatus), default=OrderStatus.CREATED, nullable=False
    )
    payment_method: Mapped[PaymentMethod] = Column(Enum(PaymentMethod), nullable=False)
    total_price: Mapped[float] = Column(Float, nullable=False)

    customer = relationship("CustomerPersistentModel", back_populates="orders")
    items = relationship("OrderItemPersistentModel", back_populates="order")


__all__ = ["OrderItemPersistentModel", "OrderPersistentModel"]
