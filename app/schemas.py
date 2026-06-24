from pydantic import BaseModel, Field


class SummarizeRequest(BaseModel):
    text: str = Field(..., min_length=20, description="The text you want summarized")
    max_words: int = Field(80, ge=10, le=500, description="Rough upper bound on summary length")


class SummarizeResponse(BaseModel):
    summary: str


class TranslateRequest(BaseModel):
    text: str = Field(..., min_length=1)
    target_language: str = Field(..., min_length=2, examples=["Hindi", "French", "Spanish"])


class TranslateResponse(BaseModel):
    translated_text: str
    target_language: str


class EmailRequest(BaseModel):
    purpose: str = Field(..., min_length=5, description="What the email should be about")
    tone: str = Field("professional", examples=["professional", "friendly", "formal"])
    recipient: str | None = Field(None, description="Who the email is addressed to")


class EmailResponse(BaseModel):
    subject: str
    body: str
