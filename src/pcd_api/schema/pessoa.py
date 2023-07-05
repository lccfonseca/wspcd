from typing import Optional
from pydantic import BaseModel

class PessoaCreate(BaseModel):
    descricao : str

class PessoaShow(BaseModel):
    id : int
    descricao : str
    
    class Config():  #tells pydantic to convert even non dict obj to json
        orm_mode = True