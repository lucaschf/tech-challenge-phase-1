from src.api.schemas import CustomerDetailsOut
from src.api.types import CPFStr
from src.core.use_cases.customer import CustomerResult

from ..presenter import Presenter


class DetailedCustomerPresenter(Presenter[CustomerDetailsOut, CustomerResult]):
    """Presenter for the CustomerDetails."""

    def present(self, data: CustomerResult) -> CustomerDetailsOut:
        """Converts the CustomerResult instance into a CustomerDetailsOut instance."""
        return CustomerDetailsOut(
            name=data.name,
            cpf=CPFStr(data.cpf.number),
            email=str(data.email),
            uuid=data.uuid,
            created_at=data.created_at,
            updated_at=data.updated_at,
        )


__all__ = ["DetailedCustomerPresenter"]
