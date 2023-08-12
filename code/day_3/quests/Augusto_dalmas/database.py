from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL= "sqlite:///./sql_app.db"
#SQLALHCEMY_DATABASE_URL = "postgresql://user:password@postgresserver/db"

#Criando um "MOTOR"
motor = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
#Instancia Banco de dados
sessionmaker = sessionmaker(autocommit=False, autoflush=False, bind=motor)
#Criação da Base
Banco = declarative_base()
