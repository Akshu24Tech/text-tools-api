import logging

from fastapi import APIRouter

from app.schemas import EmailRequest, EmailResponse
from app.services import llm

router = APIRouter()
log = logging.getLogger("app.email")


@router.post("/generate-email", response_model=EmailResponse)
def generate_email(req: EmailRequest):
    log.info("generate-email: tone=%s", req.tone)
    to_line = f" Address it to {req.recipient}." if req.recipient else ""
    prompt = (
        f"Write a {req.tone} email about: {req.purpose}.{to_line}\n"
        f"Use exactly this format:\n"
        f"Subject: <subject line>\n\n<email body>"
    )
    return _parse_email(llm.ask(prompt))


def _parse_email(raw: str) -> EmailResponse:
    subject = "(no subject)"
    body = raw
    if raw.lower().startswith("subject:"):
        first_line, _, rest = raw.partition("\n")
        subject = first_line.split(":", 1)[1].strip()
        body = rest.strip()
    return EmailResponse(subject=subject, body=body)
