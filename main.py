from sqlalchemy import create_engine,Column, Integer, Float, String, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker, relationship

Base = declarative_base ()

class Fornecedor(Base):
    __tablename__ = "frnecedores"

    id 