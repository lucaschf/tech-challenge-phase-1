from src.api.presenters.pydantic_presenter import PydanticPresenter
from src.api.schemas import OrderCreationOut
from src.core.use_cases.order import CheckoutResult


class OrderCreatedPresenter(PydanticPresenter):
    """Presenter for the OrderCreated use case."""

    def present(self, data: CheckoutResult) -> OrderCreationOut:
        """Converts the CheckoutResult instance into an OrderCreationOut instance."""
        return OrderCreationOut(number=data.number)


__all__ = ["OrderCreatedPresenter"]
