from fastapi import APIRouter

from pcd_api.api.v1.endpoints import deficiencia

from pcd_api.api.v1.endpoints import pessoa

api_router = APIRouter()

api_router.include_router(
    deficiencia.router, tags=["crud_deficiencia"], prefix="/deficiencia"
)
api_router.include_router(
    pessoa.router, tags=["crud_pessoa"], prefix="/pessoa"
)