from sqlalchemy import create_engine, Column, Integer, Float, String, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker, relationship

Base = declarative_base()

class Fornecedor(Base):
    __tablename__ = "fornecedores"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(100), nullable=False)
    idade = Column(Integer, nullable=False) 
    email = Column(String(100), nullable=False)

    produtos = relationship("Produto", back_populates="fornecedor")

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

    fornecedor_id = Column(Integer, ForeignKey("fornecedores.id"))

    fornecedor = relationship("Fornecedor", back_populates="produtos")

    def __init__(self, nome, preco, categoria):
        self.nome = nome
        self.preco = preco
        self.categoria = categoria

    def __repr__(self):
        return f"Produto: id={self.id} - nome={self.nome} - preco={self.preco} - categoria={self.categoria}"


engine = create_engine("sqlite:///negocios.db")
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)





def cadastrar_fornecedor():
    with Session() as session:
        try:
            nome_fornecedor = input("Digite o nome do fornecedor: ").capitalize()
            idade = input("Digite o nome do fornecedor: ").capitalize()
            fornecedor =  Fornecedor(nome=nome_fornecedor, idade=idade, preco=)
            session.add(fornecedor)
            session.commit()
            print(f"Fornecedor {nome_fornecedor} cadastrado com sucesso!!")
        except Exception as erro:
            session.rollback()
            print(f"Ocorreu um erro {erro}")




def cadastrar_produto():
    with Session() as session:
        try:
            nome_fornecedor = input("Digite o nome do Fornecedor para cadatrar o Produto: ").capitalize()
            fornecedor = session.query(Fornecedor).filter_by(nome=nome_fornecedor).first()
            if fornecedor == None:
                print(f"Nenhum fornecedor encontrado com esse nome {nome_fornecedor}")
                return
            else:
                nome_produto = input("Digite o nome do produto para cadatrar: ").capitalize()
                produto = Produto(nome=nome_produto)
                produto.fornecedor.append(produto)
            
                session.add(produto)
                session.commit(produto)

                print(f"Produto cadastrado com sucesso!")
        except Exception as erro:
            session.rollback()
            print(f"Ocorreu um erro {erro}")
# cadastrar_produto()
