import os

# make sure config doesn't blow up on import during tests
os.environ.setdefault("GEMINI_API_KEY", "test-key")
