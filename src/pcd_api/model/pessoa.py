from sqlalchemy import Column, Integer, String
from pcd_api.model.base import Base

class Pessoa(Base):
    
    __tablename__ = "pessoa"

    id = Column(Integer, primary_key = True, index = True)
    nome = Column(String(100))
    cpf = Column(Integer)
    cid = Column(String(15))
    email = Column(String(80))
    dt_cadastro = Column(String(10))
    deficiencia_id = Column(Integer)
    senha = Column(String(80))

