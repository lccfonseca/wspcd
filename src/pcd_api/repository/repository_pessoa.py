
from fastapi import HTTPException
from sqlalchemy.orm import Session

from pcd_api.core.config import Settings as st
from pcd_api.model.pessoa import Pessoa


def list_pessoas(db: Session):
    with db:
        try:
            health_insurer = db.query(pessoa).all()
            return health_insurer
        except Exception as err:
            #logger.error(st.project_name+':::'+f"Erro na conexão com o Banco de Dados: " + str(err))
            return HTTPException(status_code = 500, detail = f"Erro na conexão com o Banco de Dados!")