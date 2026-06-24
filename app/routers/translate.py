import logging

from fastapi import APIRouter

from app.schemas import TranslateRequest, TranslateResponse
from app.services import llm

router = APIRouter()
log = logging.getLogger("app.translate")


@router.post("/translate", response_model=TranslateResponse)
def translate(req: TranslateRequest):
    log.info("translate -> %s", req.target_language)
    prompt = (
        f"Translate the following text into {req.target_language}. "
        f"Return only the translation, no notes or explanation.\n\n{req.text}"
    )
    result = llm.ask(prompt)
    return TranslateResponse(translated_text=result, target_language=req.target_language)
