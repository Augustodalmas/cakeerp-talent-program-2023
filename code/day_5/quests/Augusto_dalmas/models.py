from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, CheckConstraint
from sqlalchemy.orm import relationship
from database import Base

class Curso(Base):
    __tablename__ = "cursos"

    id: int = Column(Integer, primary_key=True, index=True, autoincrement=True)
    titulo: str = Column(String(100), nullable=False)
    descricao: str = Column(String(255), nullable=False)
    carga_horaria: int = Column(Integer, nullable=False)
    qtd_exercicios: int = Column(Integer, nullable=False)
    curso_ativo: bool = Column(Boolean, nullable=False)
    
    alunos = relationship("Alunos", back_populates="curso")

    __table_args__ = (
        CheckConstraint(curso_ativo.in_([True, False]), name='chk_curso_ativo'),
    )


class Alunos(Base):
    __tablename__ = "alunos"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, nullable=False)
    sobrenome = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    idade = Column(Integer, nullable=False)
    cpf = Column(String, unique=True, nullable=False)
    id_curso = Column(Integer, ForeignKey("cursos.id"), nullable=False)

    curso = relationship("Curso", back_populates="alunos")