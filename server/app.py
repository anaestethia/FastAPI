from fastapi import FastApi

from.api import api_router

app = FastApi()

#incluimos el router principal a la instancia de fastapi
app.include_router(api_router)