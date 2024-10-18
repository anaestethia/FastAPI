from fastapi import APIRouter

router = APIRouter(prefix="/projects")

@router.get("/") # /projects/
async def get_all():
    return []