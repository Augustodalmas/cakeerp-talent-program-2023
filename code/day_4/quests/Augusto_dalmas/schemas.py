from pydantic import BaseModel

class CursoBase(BaseModel):
    id: int
    titulo: str
    descricao: str
    carga_horaria: int
    qtd_exercicios: int

class CursoRequest(CursoBase):
    ...

class CursoResponse(CursoBase):
    id: int

    class Config:
        from_attributes = True
        orm_mode = True
