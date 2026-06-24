from fastapi.testclient import TestClient

from app import main
from app.services import llm


client = TestClient(main.app)


def test_health():
    r = client.get("/health")
    assert r.status_code == 200
    assert r.json() == {"status": "ok"}


def test_summarize(monkeypatch):
    monkeypatch.setattr(llm, "ask", lambda prompt: "A short summary.")
    r = client.post("/summarize", json={"text": "x" * 50, "max_words": 30})
    assert r.status_code == 200
    assert r.json()["summary"] == "A short summary."


def test_summarize_rejects_short_text():
    r = client.post("/summarize", json={"text": "too short"})
    assert r.status_code == 422


def test_translate(monkeypatch):
    monkeypatch.setattr(llm, "ask", lambda prompt: "Bonjour")
    r = client.post("/translate", json={"text": "Hello", "target_language": "French"})
    assert r.status_code == 200
    body = r.json()
    assert body["translated_text"] == "Bonjour"
    assert body["target_language"] == "French"


def test_generate_email(monkeypatch):
    monkeypatch.setattr(
        llm, "ask", lambda prompt: "Subject: Leave Request\n\nHi, I'd like to apply for leave."
    )
    r = client.post("/generate-email", json={"purpose": "apply for two days leave"})
    assert r.status_code == 200
    body = r.json()
    assert body["subject"] == "Leave Request"
    assert "leave" in body["body"].lower()
