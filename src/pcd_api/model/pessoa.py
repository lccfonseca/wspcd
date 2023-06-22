from sqlalchemy import Column, Integer, String
from pcd_api.model.base import Base

class Pessoa(Base):
    
    __tablename__ = "pessoa"

    id = Column(Integer, primary_key = True, index = True)
    Nome = Column(String(60))
    cpf = Column(Integer)
    email = Column(String(100))
    cid = Column(String(15))
    senha = Column(String(80))
    dt_cadastro = Column(Integer)
    deficiencia_id = Column(Integer)