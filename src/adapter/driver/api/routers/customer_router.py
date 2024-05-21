from http import HTTPStatus

from fastapi import APIRouter, Depends, Response
from sqlalchemy.orm import Session

from src.adapter.driven.infra.config import get_db_session
from src.adapter.driven.infra.repositories import SQACustomerRepository
from src.core.application.use_cases import CustomerUserCaseImpl

from ..controllers import CustomerController
from ..schemas import CustomerCreationIn, CustomerOut
from ..schemas.http_error import HttpErrorOut
from ..types import CPFStr

router = APIRouter(tags=["Customer"], prefix="/customer")


def customer_controller_dependency(
    db_session: Session = Depends(get_db_session),  # noqa: B008
) -> CustomerController:
    customer_repository = SQACustomerRepository(db_session)
    customer_use_case = CustomerUserCaseImpl(customer_repository)
    return CustomerController(customer_use_case)


@router.post(
    "/",
    status_code=HTTPStatus.CREATED,
    responses={400: {"model": HttpErrorOut}},
    description="Creates a new customer in the system. Accepts a request body with the customer's "
    "name, CPF, and email.",
)
def create_customer(
    response: Response,
    inputs: CustomerCreationIn,
    controller: CustomerController = Depends(customer_controller_dependency),  # noqa: B008
) -> CustomerOut:
    customer = controller.create_customer(inputs)
    response.headers["Location"] = f"{router.prefix}/{customer.cpf}"
    return customer


@router.get(
    "/{cpf}",
    responses={404: {"model": HttpErrorOut}, 400: {"model": HttpErrorOut}},
    description="Retrieves a customer from the system using their CPF. The CPF is passed as a path "
    "parameter.",
)
def get_by_cpf(
    cpf: CPFStr,
    controller: CustomerController = Depends(customer_controller_dependency),  # noqa: B008
) -> CustomerOut:
    return controller.get_by_cpf(cpf)


__all__ = ["router"]
