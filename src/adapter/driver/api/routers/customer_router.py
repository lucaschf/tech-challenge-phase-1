from http import HTTPStatus

from fastapi import APIRouter, Depends, Response

from ..controllers import CustomerController
from ..dependencies import injector
from ..schemas import CustomerCreationIn, CustomerOut
from ..schemas.http_error import HttpErrorOut
from ..types import CPFStr

router = APIRouter(tags=["Customer"], prefix="/customer")


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
    controller: CustomerController = Depends(  # noqa: B008
        lambda: injector.get(CustomerController)
    ),
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
    controller: CustomerController = Depends(  # noqa: B008
        lambda: injector.get(CustomerController)
    ),
) -> CustomerOut:
    return controller.get_by_cpf(cpf)


__all__ = ["router"]
