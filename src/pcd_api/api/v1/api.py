from fastapi import APIRouter

from pcd_api.api.v1.endpoints import deficiencia

api_router = APIRouter()

api_router.include_router(
    deficiencia.router, tags=["crud_deficiencia"], prefix="/deficiencia"
)