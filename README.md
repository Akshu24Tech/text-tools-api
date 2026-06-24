# Text Tools API

A small REST API that does three text jobs using Google's Gemini model:

- `POST /summarize` — summarize a block of text
- `POST /translate` — translate text into a target language
- `POST /generate-email` — draft an email from a short brief

Built with FastAPI. Request validation, logging, exception handling and
environment-based config are all in place.

## Project layout

```
app/
  main.py            # app setup, router wiring, health check
  config.py          # settings loaded from .env
  schemas.py         # request/response models (validation lives here)
  routers/           # one file per endpoint
  services/llm.py    # thin Gemini wrapper
  core/              # logging + exception handling
tests/               # pytest tests (LLM is mocked, no key needed)
docs/API.md          # endpoint reference with examples
```

## Setup

You need Python 3.10+ and a Gemini API key (free from
https://aistudio.google.com/app/apikey).

```bash
python -m venv .venv
.venv\Scripts\activate          # on Windows
# source .venv/bin/activate     # on macOS/Linux

pip install -r requirements.txt

copy .env.example .env          # then open .env and paste your key
```

## Run

```bash
uvicorn app.main:app --reload
```

Then open http://127.0.0.1:8000/docs for the interactive Swagger UI.

## Config

Set in `.env` (see `.env.example`):

| Variable         | Default            | What it does               |
|------------------|--------------------|----------------------------|
| `GEMINI_API_KEY` | —                  | your Gemini key (required) |
| `GEMINI_MODEL`   | `gemini-1.5-flash` | which model to call        |
| `LOG_LEVEL`      | `INFO`             | log verbosity              |

## Tests

```bash
pytest
```

Tests mock the Gemini call, so they run without a real key.

## Notes

- Logs go to the console and to `logs/app.log` (rotated).
- Full endpoint reference with request/response examples is in [docs/API.md](docs/API.md).
