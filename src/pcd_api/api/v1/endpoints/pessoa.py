from fastapi import APIRouter, HTTPException
from fastapi import Depends
from sqlalchemy.orm import Session

from pcd_api.db.init_db_mysql import get_db
from pcd_api.repository.repository_pessoa import list_pessoas

router = APIRouter()

@router.get("/")
async def list_all_health_insurer(db: Session = Depends(get_db)):
    try:
        health_insurer = list_pessoas(db=db)
    except Exception:
        raise HTTPException(status_code=500, detail="Erro ao buscar lista de pessoas")
    else:
        return health_insurer