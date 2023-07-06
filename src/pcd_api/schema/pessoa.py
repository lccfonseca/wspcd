from typing import Optional
from datetime import date
from pydantic import BaseModel

class PessoaCreate(BaseModel):
    nome:str
    cpf:int
    email:str
    dt_cadastro: date
    senha:str
    cid:str
    deficiencia_id:int
    
class PessoaShow(BaseModel):
    id : int
    nome:str
    cpf:int
    email:str
    dt_cadastro:date
    deficiencia_id:int
    cid:str
    senha:str
    class Config():  #tells pydantic to convert even non dict obj to json
        orm_mode = True