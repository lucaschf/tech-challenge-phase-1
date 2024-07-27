from src.api.schemas import CustomerSummaryOut, OrderItemOut, OrderOut
from src.api.types import CPFStr
from src.core.use_cases.order import OrderResult

from ..presenter import Presenter


class OrderDetailsPresenter(Presenter[OrderOut, OrderResult]):
    """Presenter for the OrderDetailsResult use case."""

    def present(self, data: OrderResult) -> OrderOut:
        """Converts the OrderDetailsResult instance into an OrderOut instance."""
        return OrderOut(
            number=data.uuid,
            customer=CustomerSummaryOut(
                name=data.customer.name,
                email=data.customer.email,
                cpf=CPFStr(data.customer.cpf),
            ),
            status=data.status,
            total_value=data.total_value,
            created_at=data.created_at,
            updated_at=data.updated_at,
            items=[
                OrderItemOut(
                    product_name=item.product_name,
                    quantity=item.quantity,
                    unit_price=item.unit_price,
                )
                for item in data.items
            ],
        )


__all__ = ["OrderDetailsPresenter"]
