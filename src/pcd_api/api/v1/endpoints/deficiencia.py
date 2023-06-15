from fastapi import APIRouter, HTTPException
from fastapi import Depends
from sqlalchemy.orm import Session

from pcd_api.db.init_db_mysql import get_db
from pcd_api.repository.deficiencia_repository import list_deficiencias

router = APIRouter()

@router.get("/")
async def list_all_deficiencia(db: Session = Depends(get_db)):
    try:        
        deficiencia = list_deficiencias(db=db)
    except Exception:
        raise HTTPException(status_code=500, detail="Erro ao buscar lista de deficiencias")
    else:
        return deficiencia