from fastapi import FastAPI
from App import models
from App.database import engine
from App.routers import cliente, fornecedor, produto, venda, compra

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Loja de Roupas - API CRUD")

app.include_router(cliente.router)
app.include_router(fornecedor.router)
app.include_router(produto.router)
app.include_router(venda.router)
app.include_router(compra.router)