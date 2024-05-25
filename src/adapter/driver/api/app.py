from fastapi import FastAPI

from src.adapter.driver.api.routers import customer_router, product_router
from src.config import settings

app = FastAPI(
    docs_url=settings.DOCS_URL,
    redoc_url=settings.REDOC_URL,
    title="Tech challenge API",
)

app.include_router(customer_router, prefix="/api")
app.include_router(product_router, prefix="/api")


@app.get("/", tags=["Health Check"])
def root() -> dict[str, str]:
    """Health check endpoint."""
    return {"status": "OK"}
