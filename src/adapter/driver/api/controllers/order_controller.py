from src.adapter.driver.api.schemas import OrderCreationIn, OrderOut
from src.core.application.use_cases.order_use_case import OrderUseCase
from src.core.domain.entities.order import Order


class OrderController:
    """This class manages order-related actions using CustomerUseCase.

    The class acts as the intersection between the API and the business logic,
    handling HTTP requests related to order data.

    Attributes:
        _order_use_case: An instance of the OrderUseCase class for
        performing operations related to order.
    """

    def __init__(self, order_use_case: OrderUseCase) -> None:
        self._order_use_case = order_use_case

    def create_order(self, order_data: OrderCreationIn) -> OrderOut:
        """Create a new order."""
        created_out: Order = self._order_use_case.create_order(order_data.to_order_input_dto())

        return OrderOut.model_validate(*created_out.__dict__)


__all__ = ["OrderController"]
