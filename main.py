from fastapi import FastAPI
from app.database.configuration import Engine
from app.api.routes.endpoints import rutas
from app.api.models.tablasSQL import Base

from starlette.responses import RedirectResponse
from starlette.middleware.cors import CORSMiddleware

Base.metadata.create_all(bind = Engine)

app = FastAPI()

#Configurar el protocolo CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins = ["*"],
    allow_credentials = True,
    allow_methods = ["*"],
    allow_headers = ["*"]
)

@app.get("/")
def main():
    return RedirectResponse(url= "/docs")

app.include_router(rutas)
