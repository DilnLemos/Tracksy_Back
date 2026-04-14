from fastapi import FastAPI
from app.db.database import engine, Base
import app.models
app = FastAPI()

@app.on_event("startup")
def on_startup():
    Base.metadata.create_all(bind=engine)
    print("Tables created successfully")


@app.get("/health")
def health():
    return {"health": "ok"}