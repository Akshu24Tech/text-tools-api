import logging

from fastapi import FastAPI

from app.config import get_settings
from app.core.exceptions import register_exception_handlers
from app.core.logging import setup_logging
from app.routers import email, summarize, translate

settings = get_settings()
setup_logging(settings.log_level)
log = logging.getLogger("app")

app = FastAPI(
    title=settings.app_name,
    description="A small REST API for text summarization, translation and email drafting, backed by Gemini.",
    version="1.0.0",
)

register_exception_handlers(app)

app.include_router(summarize.router, tags=["summarize"])
app.include_router(translate.router, tags=["translate"])
app.include_router(email.router, tags=["email"])

log.info("%s ready", settings.app_name)


@app.get("/health", tags=["health"])
def health():
    return {"status": "ok"}
