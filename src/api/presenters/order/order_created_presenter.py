from src.api.presenters.pydantic_presenter import PydanticPresenter
from src.api.schemas import OrderCreationOut
from src.core.use_cases.order import OrderResult


class OrderCreatedPresenter(PydanticPresenter[OrderResult, OrderCreationOut]):
    """Presenter for the OrderCreated use case."""

    def present(self, data: OrderResult) -> OrderCreationOut:
        """Converts the OrderResult instance into an OrderCreationOut instance."""
        return OrderCreationOut(number=data.uuid)


__all__ = ["OrderCreatedPresenter"]
