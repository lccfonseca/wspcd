from fastapi import HTTPException
from sqlalchemy.orm import Session

from pcd_api.core.config import Settings as st
from pcd_api.model.pessoa import Pessoa


def list_pessoas(db: Session):
    with db:
        try:
            health_insurer = db.query(Pessoa).all()
            return health_insurer
        except Exception as err:
            # logger.error(st.project_name+':::'+f"Erro na conexão com o Banco de Dados: " + str(err))
            return HTTPException(status_code=500, detail=f"Erro na conexão com o Banco de Dados!")


def retrieve_pessoa_by_id(id: int, db: Session):
    with db:
        try:
            item = db.query(Pessoa).filter(Pessoa.id == id).first()
            return item
        except Exception as err:
            # logger.exception(st.PROJECT_NAME+':::'+f"Erro na conexão com o Banco de Dados: " + str(err))
            return err


def create_new_pessoa(pessoa: Pessoa, db: Session):
    with db:
        try:
            pessoa_obj = Pessoa(**pessoa.dict())
            db.add(pessoa_obj)
            db.commit()
            db.refresh(pessoa_obj)
            return pessoa_obj
        except Exception as err:
            # logger.exception(st.PROJECT_NAME+':::'+f"Erro na conexão com o Banco de Dados: " + str(err))
            return err


def update_pessoa_by_id(id: int, pessoa: Pessoa, db: Session):
    with db:
        try:
            existing_pessoa = db.query(Pessoa).filter(Pessoa.id == id)
            if not existing_pessoa.first():
                return 0
            existing_pessoa.update(pessoa.__dict__)
            db.commit()
            return 1
        except Exception as err:
            # logger.exception(st.PROJECT_NAME+':::'+f"Erro na conexão com o Banco de Dados: " + str(err))
            return err


def delete_pessoa_by_id(id: int, db: Session):
    with db:
        try:
            existing_pessoa = db.query(Pessoa).filter(Pessoa.id == id)
            if not existing_pessoa.first():
                return 0
            existing_pessoa.delete(synchronize_session=False)
            db.commit()
            return 1
        except Exception as err:
            # logger.exception(st.PROJECT_NAME+':::'+f"Erro na conexão com o Banco de Dados: " + str(err))
            return err