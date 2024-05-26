import traceback
from http import HTTPStatus
from typing import Callable, Coroutine

from fastapi import FastAPI, Request, Response
from starlette.responses import JSONResponse

from src.adapter.driver.api.routers import customer_router, product_router
from src.config import settings
from src.core.domain.exceptions import DomainError, NotFoundError

app = FastAPI(
    docs_url=settings.DOCS_URL,
    redoc_url=settings.REDOC_URL,
    title="Tech challenge API",
)


async def _exception_middleware(
    request: Request, call_next: Callable[[Request], Coroutine[None, None, Response]]
) -> Response:
    """Asynchronous middleware function to handle exceptions in the FastAPI application.

    This function catches exceptions raised during the processing of a request and
    returns an appropriate HTTP response.

    Args:
        request: The FastAPI Request object representing the incoming request.
        call_next: A coroutine function that, when awaited, will call the next middleware or
         endpoint.

    Returns:
        A Response object containing the HTTP response to be sent back to the client.
    """
    try:
        return await call_next(request)
    except Exception as e:
        return handle_error(e)


def handle_error(e: Exception) -> Response:
    """Handle exceptions that are raised during the processing of a request.

    This function checks if the exception is an instance of `DomainError`.
    If it is, it returns a JSON response with a
    status code of `BAD_REQUEST` and a detail message from the exception.

    If the exception is not a `DomainError`, it returns a JSON response with a status code of
    `INTERNAL_SERVER_ERROR` and a generic detail message.

    Args:
        e (Exception): The exception that was raised.

    Returns:
        Response:
        A FastAPI Response object containing the HTTP response to be sent back to the client.
    """
    if isinstance(e, NotFoundError):
        return JSONResponse(
            status_code=HTTPStatus.NOT_FOUND,
            content={"detail": e.message},
        )

    if isinstance(e, DomainError):
        return JSONResponse(
            status_code=HTTPStatus.BAD_REQUEST,
            content={"detail": e.message},
        )

    traceback.print_exc()
    return JSONResponse(
        status_code=HTTPStatus.INTERNAL_SERVER_ERROR,
        content={"detail": "Internal server error."},
    )


app.include_router(customer_router, prefix="/api")
app.include_router(product_router, prefix="/api")
app.middleware("http")(_exception_middleware)


@app.get("/", tags=["Health Check"])
def root() -> dict[str, str]:
    """Health check endpoint."""
    return {"status": "OK"}
