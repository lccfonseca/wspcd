from typing import Optional
from datetime import date
from pydantic import BaseModel


class PessoaCreate(BaseModel):
    nome : str
    cpf : int
    email : str
    cid : str
    senha : str
    dt_cadastro : date
    deficiencia_id : int

class PessoaShow(BaseModel):
    id: int
    nome : str
    cpf : int
    email : str
    cid : str
    senha : str
    dt_cadastro : date
    deficiencia_id : int
    class Config():  # tells pydantic to convert even non dict obj to json
        orm_mode = True