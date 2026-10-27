
"""Application REST développée avec FastAPI."""

from fastapi import FastAPI

app = FastAPI(title="LearningPython API")


@app.get("/")
def home():
    """Retourner un message de bienvenue."""
    return {"message": "Bienvenue sur mon API Python !"}


@app.get("/health")
def health():
    """Vérifier que l'API fonctionne."""
    return {"status": "ok"}
