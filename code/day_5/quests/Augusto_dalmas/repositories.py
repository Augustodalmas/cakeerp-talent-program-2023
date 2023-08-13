from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from models import Curso, Alunos
from schemas import CursoResponse, AlunoResponse

class CursoRepository:
    @staticmethod
    def find_all(db: Session) -> list[Curso]:
        return db.query(Curso).all()

    @staticmethod
    def save(db: Session, curso: Curso) -> Curso:
        if curso.id:
            db.merge(curso)
        else:
            db.add(curso)
        db.commit()
        return curso

    @staticmethod
    def find_by_id(db: Session, id: int) -> Curso:
        return db.query(Curso).filter(Curso.id == id).first()

    @staticmethod
    def exists_by_id(db: Session, id: int) -> bool:
        return db.query(Curso).filter(Curso.id == id).first() is not None

    @staticmethod
    def delete_by_id(db: Session, id: int) -> None:
        curso = db.query(Curso).filter(Curso.id == id).first()
        if curso is not None:
            db.delete(curso)
            db.commit()

    @staticmethod
    def update(db: Session, curso: Curso, request_data: CursoResponse):
        for key, value in request_data.dict().items():
            setattr(curso, key, value)
        
        db.commit()
        db.refresh(curso)
        
        return curso
    

    @staticmethod
    def curso_ativo(db: Session, curso_id: int) -> bool:
        curso = db.query(Curso).filter(Curso.id == curso_id).first()
        if curso is None:
            return False
        return curso.curso_ativo


class AlunoRepository:
    @staticmethod
    def find_all(db: Session) -> list[Alunos]:
        return db.query(Alunos).all()

    @staticmethod
    def save(db: Session, aluno: Alunos) -> Alunos:
        if aluno.id:
            db.merge(aluno)
        else:
            db.add(aluno)
        db.commit()
        return aluno


    @staticmethod
    def find_by_id(db: Session, id: int) -> Alunos:
        return db.query(Alunos).filter(Alunos.id == id).first()


    @staticmethod
    def exists_by_id(db: Session, id: int) -> bool:
        return db.query(Alunos).filter(Alunos.id == id).first() is not None


    @staticmethod
    def delete_by_id(db: Session, id: int) -> None:
        aluno = db.query(Alunos).filter(Alunos.id == id).first()
        if aluno is not None:
            curso_id = aluno.id_curso
            if CursoRepository.curso_ativo(db, curso_id):
                raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Não foi possível excluir o aluno, pois ele está vinculado a um curso ativo.")
            db.delete(aluno)
            db.commit()


    @staticmethod
    def update(db: Session, aluno: Alunos, request_data: AlunoResponse):
        for key, value in request_data.dict().items():
            setattr(aluno, key, value)
        
        db.commit()
        db.refresh(aluno)
        
        return aluno