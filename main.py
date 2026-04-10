from sqlalchemy import create_engine,Column, Integer, Float, String, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker, relationship

Base = declarative_base ()

class Fornecedor(Base):
    __tablename__ = "fornecedores"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(100), nullable=False,)
    idade = Column(String(100), nullable=False,)
    email = Column(String(100), nullable=False, )

    produtos = relationship("Produto", back_populates= "produtos")

    

    def __init__(self, nome, idade, email):
        self.nome = nome
        self.idade = idade
        self.email = email

    def __repr__(self):
        return f"Fornecedor: id={self.id} - nome={self.nome} - idade={self.idade} - email={self.email}"
    
class Produto(Base):
    __tablename__ = "produtos"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(100), nullable=False)
    preco = Column(Float)
    categoria = Column(String(100))

    fornecedores_id = Column(Integer, ForeignKey("fornecedores_id"))

    fornecedores = relationship("Fornecedor", back_populates="fornecedores")

    def __init__(self, nome, preco, categoria):
        self.nome = nome
        self.preco = preco
        self.categoria = categoria

    def __repr__(self):
        return f"Produto: id={self.id} - nome={self.nome} - preco={self.preco} - categoraia={self.categoria}"
    

engine = create_engine("sqlite://Negócios.db")

Base.matadata.create_all(engine)

Session = sessionmaker(bing=engine)



