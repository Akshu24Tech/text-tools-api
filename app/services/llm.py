import logging

import google.generativeai as genai

from app.config import get_settings
from app.core.exceptions import LLMError

log = logging.getLogger("app.llm")

_configured = False


def _get_model():
    global _configured
    settings = get_settings()
    if not _configured:
        genai.configure(api_key=settings.gemini_api_key)
        _configured = True
        log.info("Gemini configured with model %s", settings.gemini_model)
    return genai.GenerativeModel(settings.gemini_model)


def ask(prompt: str) -> str:
    """Send a single prompt to Gemini and return the trimmed text reply."""
    try:
        response = _get_model().generate_content(prompt)
        return response.text.strip()
    except Exception as exc:
        raise LLMError(str(exc)) from exc
