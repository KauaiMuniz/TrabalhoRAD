from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from App import crud, schemas, database

router = APIRouter(prefix="/produtos", tags=["Produtos"])

@router.post("/", response_model=schemas.ProdutoResponse)
def create_produto_route(produto: schemas.ProdutoCreate, db: Session = Depends(database.get_db)):
    return crud.create_produto(db, produto)

@router.get("/", response_model=list[schemas.ProdutoResponse])
def read_produtos(db: Session = Depends(database.get_db)):
    return crud.get_produtos(db)

@router.get("/{id}", response_model=schemas.ProdutoResponse)
def read_produto(id: int, db: Session = Depends(database.get_db)):
    produto = crud.get_produto(db, id)
    if not produto:
        raise HTTPException(status_code=404, detail="Produto não encontrado")
    return produto

@router.put("/{id}", response_model=schemas.ProdutoResponse)
def update_produto_route(id: int, produto: schemas.ProdutoCreate, db: Session = Depends(database.get_db)):
    return crud.update_produto(db, id, produto)

@router.delete("/{id}")
def delete_produto_route(id: int, db: Session = Depends(database.get_db)):
    crud.delete_produto(db, id)
    return {"message": "Produto excluído"}

@router.delete("/")
def delete_all_produtos_route(db: Session = Depends(database.get_db)):
    crud.delete_all_produtos(db)
    return {"message": "Todos os produtos excluídos"}