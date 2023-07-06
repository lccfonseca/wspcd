from fastapi import APIRouter, HTTPException, status
from fastapi import Depends
from sqlalchemy.orm import Session

from pcd_api.db.init_db_mysql import get_db
from pcd_api.repository.pessoa_repository import list_pessoas, retrieve_pessoa_by_id, create_new_pessoa, update_pessoa_by_id, delete_pessoa_by_id
from pcd_api.schema.pessoa import PessoaCreate, PessoaShow

router = APIRouter()

@router.get("/")
async def list_all_pessoas(db: Session = Depends(get_db)):
    try:        
        pessoa = list_pessoas(db=db)
    except Exception:
        raise HTTPException(status_code=500, detail="Erro ao buscar lista de pessoas")
    else:
        return pessoa

@router.get("/{id}", response_model=PessoaShow)
async def retrieve_pessoa(id:int, db: Session = Depends(get_db)):
    pessoa = retrieve_pessoa_by_id(id=id, db=db)
    if not pessoa:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"pessoa with this id {id} does not exist")
    return pessoa

@router.post("/")
async def create_pessoa(pessoa: PessoaCreate, db: Session = Depends(get_db)):
    pessoa = create_new_pessoa(pessoa=pessoa, db=db)
    return pessoa

@router.put("/{id}")
async def update_pessoa(id: int, pessoa:PessoaCreate, db: Session = Depends(get_db)):
    updated = update_pessoa_by_id(id=id, pessoa=pessoa, db=db)
    if not updated:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Pessoa with id {id} not found")
    return {"msg":"Successfully updated data."}

@router.delete("/{id}")
async def delete_pessoa(id: int, db: Session = Depends(get_db)):
    deleted = delete_pessoa_by_id(id=id, db=db)
    if not deleted:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Pessoa with id {id} not found")
    return {"msg":"Successfully deleted."}