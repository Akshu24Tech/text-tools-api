import logging

from fastapi import APIRouter

from app.schemas import SummarizeRequest, SummarizeResponse
from app.services import llm

router = APIRouter()
log = logging.getLogger("app.summarize")


@router.post("/summarize", response_model=SummarizeResponse)
def summarize(req: SummarizeRequest):
    log.info("summarize: %d chars, max_words=%d", len(req.text), req.max_words)
    prompt = (
        f"Summarize the text below in at most {req.max_words} words. "
        f"Keep the main points and write in plain English.\n\n{req.text}"
    )
    return SummarizeResponse(summary=llm.ask(prompt))
