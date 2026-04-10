from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from App import crud, models, schemas, database

router = APIRouter(prefix="/produtos", tags=["Produtos"])

@router.post("/", response_model=schemas.ProdutoResponse)
def create_produto(produto: schemas.ProdutoCreate, db: Session = Depends(database.get_db)):
    return crud.create_item(db, models.Produto, produto.dict())

@router.get("/", response_model=list[schemas.ProdutoResponse])
def read_produtos(db: Session = Depends(database.get_db)):
    return crud.get_items(db, models.Produto)

@router.get("/{id}", response_model=schemas.ProdutoResponse)
def read_produto(id: int, db: Session = Depends(database.get_db)):
    produto = crud.get_item(db, models.Produto, id)
    if not produto: raise HTTPException(status_code=404, detail="Produto não encontrado")
    return produto

@router.put("/{id}", response_model=schemas.ProdutoResponse)
def update_produto(id: int, produto: schemas.ProdutoCreate, db: Session = Depends(database.get_db)):
    return crud.update_item(db, models.Produto, id, produto.dict())

@router.delete("/{id}")
def delete_produto(id: int, db: Session = Depends(database.get_db)):
    crud.delete_item(db, models.Produto, id)
    return {"message": "Produto excluído"}

@router.delete("/")
def delete_all_produtos(db: Session = Depends(database.get_db)):
    crud.delete_all(db, models.Produto)
    return {"message": "Todos os produtos excluídos"}