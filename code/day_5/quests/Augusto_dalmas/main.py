from fastapi import FastAPI, Depends, HTTPException, status, Response
from sqlalchemy.orm import Session
from fastapi.openapi.utils import get_openapi
from models import Curso, Alunos
from database import engine, Base, get_db
from repositories import CursoRepository, AlunoRepository
from schemas import CursoRequest, CursoResponse, AlunoRequest, AlunoResponse

Base.metadata.create_all(bind=engine)

app = FastAPI()
#--------------------------------------------AREA DO CURSO--------------------------------------------------------
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

#--------------------------------------------AREA DO ALUNO--------------------------------------------------------
#Criar um novo aluno
@app.post("/api/alunos", response_model=AlunoResponse, status_code=status.HTTP_201_CREATED)
def create(request: AlunoRequest, db: Session = Depends(get_db)):
    aluno = AlunoRepository.save(db, Alunos(**request.dict()))
    
    return AlunoResponse.from_orm(aluno)

#Procurar todos os alunos
@app.get("/api/alunos", response_model=list[AlunoResponse])
def find_all(db: Session = Depends(get_db)):
    alunos = AlunoRepository.find_all(db)
    return [AlunoResponse.from_orm(aluno) for aluno in alunos]

# Filtrar um aluno por ID
@app.get("/api/alunos{aluno_id}", response_model=AlunoResponse)
def find_aluno_by_id(aluno_id: int, db: Session = Depends(get_db)):
    aluno = AlunoRepository.find_by_id(db, aluno_id)
    if not aluno:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="aluno não encontrado")
    return AlunoResponse.from_orm(aluno)

# Remover um aluno
@app.delete("/api/alunos{aluno_id}", response_model=AlunoResponse)
def delete_aluno(aluno_id: int, db: Session = Depends(get_db)):
    aluno = AlunoRepository.delete_by_id(db, aluno_id)
    if not aluno:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="aluno não encontrado")
    return AlunoResponse.from_orm(aluno)

# Atualizar dados de um aluno
@app.put("/api/alunos{aluno_id}", response_model=AlunoResponse)
def update_aluno(aluno_id: int, request: AlunoResponse, db: Session = Depends(get_db)):
    aluno = db.query(Alunos).filter(Alunos.id == aluno_id).first()
    if not aluno:
        raise HTTPException(status_code=404, detail="aluno não encontrado")
    
    aluno = AlunoRepository.update(db, aluno, request)
    
    return aluno

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
