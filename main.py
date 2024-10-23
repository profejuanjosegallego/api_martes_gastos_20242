from fastapi import FastAPI
from app.database.configuration import engine
from app.api.routes.endpoints import rutas
from app.api.models.tablasSQL import Base

from starlette.responses import RedirectResponse

Base.metadata.create_all(bind = engine)

app = FastAPI()

@app.get("/")
def main():
    return RedirectResponse(url= "/docs")

app.include_router(rutas)
