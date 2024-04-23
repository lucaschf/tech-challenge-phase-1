from fastapi import FastAPI

from src.config import settings

app = FastAPI(docs_url=settings.DOCS_URL, redoc_url=settings.REDOC_URL)


@app.get("/", tags=["Health Check"])
def root() -> dict[str, str]:
    """Health check endpoint."""
    return {"status": "OK"}
