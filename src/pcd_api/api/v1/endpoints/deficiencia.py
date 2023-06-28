from fastapi import APIRouter, HTTPException, status
from fastapi import Depends
from sqlalchemy.orm import Session

from pcd_api.db.init_db_mysql import get_db
from pcd_api.repository.deficiencia_repository import list_deficiencias, retrieve_deficiencia_by_id, create_new_deficiencia, update_deficiencia_by_id, delete_deficiencia_by_id
from pcd_api.schema.deficiencia import DeficienciaCreate, DeficienciaShow

router = APIRouter()

@router.get("/")
async def list_all_deficiencia(db: Session = Depends(get_db)):
    try:        
        deficiencia = list_deficiencias(db=db)
    except Exception:
        raise HTTPException(status_code=500, detail="Erro ao buscar lista de deficiencias")
    else:
        return deficiencia
    
@router.get("/{id}", response_model=DeficienciaShow)
async def retrieve_deficiencia(id:int, db: Session = Depends(get_db)):
    deficiencia = retrieve_deficiencia_by_id(id=id, db=db)
    if not deficiencia:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Deficiencia with this id {id} does not exist")
    return deficiencia

@router.post("/", response_model=DeficienciaShow)
async def create_deficiencia(deficiencia: DeficienciaCreate, db: Session = Depends(get_db)):
    deficiencia = create_new_deficiencia(deficiencia=deficiencia, db=db)
    return deficiencia

@router.put("/{id}")
async def update_deficiencia(id: int, deficiencia:DeficienciaCreate, db: Session = Depends(get_db)):
    updated = update_deficiencia_by_id(id=id, deficiencia=deficiencia, db=db)
    if not updated:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Deficiencia with id {id} not found")
    return {"msg":"Successfully updated data."}

@router.delete("/{id}")
async def delete_deficiencia(id: int, db: Session = Depends(get_db)):
    deleted = delete_deficiencia_by_id(id=id, db=db)
    if not deleted:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Deficiencia with id {id} not found")
    return {"msg":"Successfully deleted."}