from sqlalchemy import Column, Integer, String, Float, ForeignKey
from .database import Base

class Cliente(Base):
    __tablename__ = "clientes"
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, index=True)
    email = Column(String)

class Fornecedor(Base):
    __tablename__ = "fornecedores"
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, index=True)
    cnpj = Column(String)

class Produto(Base):
    __tablename__ = "produtos"
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, index=True)
    preco = Column(Float)

class Compra(Base):
    __tablename__ = "compras"
    id = Column(Integer, primary_key=True, index=True)
    produto_id = Column(Integer, ForeignKey("produtos.id"))
    quantidade = Column(Integer)

class Venda(Base):
    __tablename__ = "vendas"
    id = Column(Integer, primary_key=True, index=True)
    produto_id = Column(Integer, ForeignKey("produtos.id"))
    quantidade = Column(Integer)