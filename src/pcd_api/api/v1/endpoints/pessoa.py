from fastapi import APIRouter, HTTPException
from fastapi import Depends
from sqlalchemy.orm import Session

from pcd_api.db.init_db_mysql import get_db
from pcd_api.repository.pessoa_repository import list_pessoa

router = APIRouter()

@router.get("/")
async def list_all_pessoa(db: Session = Depends(get_db)):
    try:        
        pessoa = list_pessoa(db=db)
    except Exception:
        raise HTTPException(status_code=500, detail="Erro ao buscar lista de pessoas")
    else:
        return pessoa