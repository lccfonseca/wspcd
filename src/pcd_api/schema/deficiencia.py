from typing import Optional
from pydantic import BaseModel

class DeficienciaCreate(BaseModel):
    descricao : str

class DeficienciaShow(BaseModel):
    id : int
    descricao : str
    
    class Config():  #tells pydantic to convert even non dict obj to json
        orm_mode = True