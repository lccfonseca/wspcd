from sqlalchemy import Column, Integer, String
from pcd_api.model.base import Base

class Deficiencia(Base):
    
    __tablename__ = "deficiencia"

    id = Column(Integer, primary_key = True, index = True)
    descricao = Column(String(45))