from fastapi import HTTPException
from sqlalchemy.orm import Session

from pcd_api.core.config import Settings as st
from pcd_api.model.deficiencia import Deficiencia


def list_deficiencias(db: Session):
    with db:
        try:    
            deficiencia = db.query(Deficiencia).all()
            return deficiencia
        except Exception as err:
            #logger.error(st.project_name+':::'+f"Erro na conexão com o Banco de Dados: " + str(err))
            return HTTPException(status_code = 500, detail = f"Erro na conexão com o Banco de Dados!")
        
def retrieve_deficiencia_by_id(id: int, db: Session):
    with db:
        try:
            item = db.query(Deficiencia).filter(Deficiencia.id == id).first()
            return item
        except Exception as err:
            #logger.exception(st.PROJECT_NAME+':::'+f"Erro na conexão com o Banco de Dados: " + str(err))
            return err
        
def create_new_deficiencia(deficiencia: Deficiencia, db: Session):
    with db:
        try:
            deficiencia_obj = Deficiencia(**deficiencia.dict())
            db.add(deficiencia_obj)
            db.commit()
            db.refresh(deficiencia_obj)
            return deficiencia_obj
        except Exception as err:
            #logger.exception(st.PROJECT_NAME+':::'+f"Erro na conexão com o Banco de Dados: " + str(err))
            return err
        
def update_deficiencia_by_id(id:int, deficiencia: Deficiencia, db: Session):
    with db:
        try:
            existing_deficiencia = db.query(Deficiencia).filter(Deficiencia.id == id)
            if not existing_deficiencia.first():
                return 0
            existing_deficiencia.update(deficiencia.__dict__)
            db.commit()
            return 1
        except Exception as err:
            #logger.exception(st.PROJECT_NAME+':::'+f"Erro na conexão com o Banco de Dados: " + str(err))
            return err
        
def delete_deficiencia_by_id(id: int, db: Session):
    with db:
        try:
            existing_deficiencia = db.query(Deficiencia).filter(Deficiencia.id == id)
            if not existing_deficiencia.first():
                return 0
            existing_deficiencia.delete(synchronize_session=False)
            db.commit()
            return 1
        except Exception as err:
            #logger.exception(st.PROJECT_NAME+':::'+f"Erro na conexão com o Banco de Dados: " + str(err))
            return err