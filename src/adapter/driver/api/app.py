from http import HTTPStatus

from fastapi import FastAPI, Request, Response
from starlette.responses import JSONResponse

from src.adapter.driver.api.routers import customer_router, product_router
from src.config import settings
from src.core.domain.base import DomainError

app = FastAPI(
    docs_url=settings.DOCS_URL,
    redoc_url=settings.REDOC_URL,
    title="Tech challenge API",
)


async def _exception_middleware(request: Request, call_next):  # noqa: ANN001, ANN202
    """Captura erros, envia-os ao Sentry e retorna um status HTTP para o usuário."""
    try:
        return await call_next(request)
    except Exception as e:
        return handle_error(e)


def handle_error(e: Exception) -> Response:
    """Handle errors, report them to Sentry, and return an HTTP response.

    Errors that are instances of ApiResponseError or HTTPException with a status code in the 400
    range are mapped and returned with their own message and status code.

    If an unhandled exception is raised, return a 500-status code.

    Args:
         e: The exception to handle.

    Returns:
         The JSONResponse containing the appropriate status code and detail.
    """
    if isinstance(e, DomainError):
        return JSONResponse(
            status_code=HTTPStatus.BAD_REQUEST,
            content={"detail": e.message},
        )

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
