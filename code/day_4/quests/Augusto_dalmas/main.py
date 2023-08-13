from fastapi import FastAPI, Depends, HTTPException, status, Response
from sqlalchemy.orm import Session
from fastapi.openapi.utils import get_openapi
from models import Curso
from database import engine, Base, get_db
from repositories import CursoRepository
from schemas import CursoRequest, CursoResponse

Base.metadata.create_all(bind=engine)

app = FastAPI()

#Criar um novo Curso
@app.post("/api/cursos", response_model=CursoResponse, status_code=status.HTTP_201_CREATED)
def create(request: CursoRequest, db: Session = Depends(get_db)):
    curso = CursoRepository.save(db, Curso(**request.dict()))
    
    return CursoResponse.from_orm(curso)

#Procurar todos os Cursos
@app.get("/api/cursos", response_model=list[CursoResponse])
def find_all(db: Session = Depends(get_db)):
    cursos = CursoRepository.find_all(db)
    return [CursoResponse.from_orm(curso) for curso in cursos]

# Filtrar um curso por ID
@app.get("/api/cursos/{curso_id}", response_model=CursoResponse)
def find_curso_by_id(curso_id: int, db: Session = Depends(get_db)):
    curso = CursoRepository.find_by_id(db, curso_id)
    if not curso:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Curso não encontrado")
    return CursoResponse.from_orm(curso)

# Remover um curso
@app.delete("/api/cursos/{curso_id}", response_model=CursoResponse)
def delete_curso(curso_id: int, db: Session = Depends(get_db)):
    curso = CursoRepository.delete_by_id(db, curso_id)
    if not curso:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Curso não encontrado")
    return CursoResponse.from_orm(curso)

# Atualizar dados de um curso
@app.put("/api/cursos/{curso_id}", response_model=CursoResponse)
def update_curso(curso_id: int, request: CursoResponse, db: Session = Depends(get_db)):
    curso = db.query(Curso).filter(Curso.id == curso_id).first()
    if not curso:
        raise HTTPException(status_code=404, detail="Curso não encontrado")
    
    curso = CursoRepository.update(db, curso, request)
    
    return curso


"""
def update_curso(curso_id: int, request: CursoUpdate, db: Session = Depends(get_db)):
    curso = db.query(Curso).filter(Curso.id == curso_id).first()
    if not curso:
        raise HTTPException(status_code=404, detail="Curso não encontrado")
    
    curso = CursoRepository.update(db, curso, request)
    
    return curso
"""
def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="Ambiente Virtual de Aprendizagem",
        version="1.0.0",
        summary="Alunos EAD",
        description="Sistema de Ambiente Virtual de Aprendizagem para auxiliar alunos 100% EAD",
        routes=app.routes,
    )
    app.openapi_schema = openapi_schema
    return app.openapi_schema


app.openapi = custom_openapi
