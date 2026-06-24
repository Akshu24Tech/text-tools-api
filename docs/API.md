# API Reference

Base URL: `http://127.0.0.1:8000`

All request and response bodies are JSON. Validation errors return `422` with
details about the offending field. If the model call fails the API returns
`502` with a short message.

Interactive docs are also auto-generated at `/docs` (Swagger) and `/redoc`.

---

## POST /summarize

Summarize a block of text.

**Request**

| Field       | Type   | Required | Notes                          |
|-------------|--------|----------|--------------------------------|
| `text`      | string | yes      | at least 20 characters         |
| `max_words` | int    | no       | 10–500, defaults to 80         |

```bash
curl -X POST http://127.0.0.1:8000/summarize \
  -H "Content-Type: application/json" \
  -d '{"text": "Long article text goes here...", "max_words": 50}'
```

**Response**

```json
{ "summary": "A concise summary of the text." }
```

---

## POST /translate

Translate text into a target language.

**Request**

| Field             | Type   | Required | Notes                  |
|-------------------|--------|----------|------------------------|
| `text`            | string | yes      | non-empty              |
| `target_language` | string | yes      | e.g. "Hindi", "French" |

```bash
curl -X POST http://127.0.0.1:8000/translate \
  -H "Content-Type: application/json" \
  -d '{"text": "Hello, how are you?", "target_language": "Hindi"}'
```

**Response**

```json
{ "translated_text": "नमस्ते, आप कैसे हैं?", "target_language": "Hindi" }
```

---

## POST /generate-email

Draft an email from a short brief.

**Request**

| Field       | Type   | Required | Notes                                       |
|-------------|--------|----------|---------------------------------------------|
| `purpose`   | string | yes      | what the email is about (min 5 chars)       |
| `tone`      | string | no       | e.g. "professional", "friendly", "formal"   |
| `recipient` | string | no       | who it's addressed to                       |

```bash
curl -X POST http://127.0.0.1:8000/generate-email \
  -H "Content-Type: application/json" \
  -d '{"purpose": "request two days of leave next week", "tone": "professional", "recipient": "my manager"}'
```

**Response**

```json
{
  "subject": "Leave Request",
  "body": "Hi,\n\nI would like to request two days of leave next week..."
}
```

---

## GET /health

Simple health check.

```json
{ "status": "ok" }
```
