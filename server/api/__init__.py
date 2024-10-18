from fastapi import APIRouter

from .v1 import router_v1

#ROUTER API
api_router =APIRouter(prefix="/api")
api_router.inlcude_router(router_v1)