from fastapi import FastAPI

from app.database import engine
from app import models
from app.routes import assets
from app.routes import maintenance

models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Smart Asset Management API",
    version="1.0.0",
    description="Backend API for managing enterprise assets and maintenance workflows."
)


@app.get("/", tags=["Health Check"])
def root():
    return {
        "message": "Smart Asset Management API is running"
    }


app.include_router(assets.router)

app.include_router(maintenance.router)