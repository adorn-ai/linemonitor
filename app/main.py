import os
from app.core.config import settings
from fastapi import FastAPI

app = FastAPI(
    title = settings.TITLE,
    version = settings.VERSION
)
@app.get("/")
def root():
    return {
        "detail": "Welcome to Monitorline's API"
    }

@app.get("/ping")
def ping():
    return {
        "detail": "API ok!"
    }