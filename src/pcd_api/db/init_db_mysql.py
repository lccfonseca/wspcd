from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from pcd_api.core.config import Settings as st

engine = create_engine(st.db_connection_string, echo=True)

SessionLocal = sessionmaker(bind=engine)

def get_db(): 
    try:
        db = SessionLocal()
        return db
    except Exception as err:
        #logger.exception(st.project_name+':::'+f"Erro na conexão com o Banco de Dados: " + str(err))
        return {'Database Connection Error': err}
        
    finally:
        db.close()