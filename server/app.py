from fastapi import FastAPI

from .api import api_router

app = FastAPI()

#incluimos el router principal a la instancia de fastapi
app.include_router(api_router)