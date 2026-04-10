from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from App import crud, models, schemas, database

router = APIRouter(prefix="/compras", tags=["Compras"])

@router.post("/", response_model=schemas.CompraResponse)
def create_compra(compra: schemas.CompraCreate, db: Session = Depends(database.get_db)):
    # Validação extra: verificar se o produto existe antes de registrar a compra
    produto = crud.get_item(db, models.Produto, compra.produto_id)
    if not produto: raise HTTPException(status_code=404, detail="Produto não encontrado")
    return crud.create_item(db, models.Compra, compra.dict())

@router.get("/", response_model=list[schemas.CompraResponse])
def read_compras(db: Session = Depends(database.get_db)):
    return crud.get_items(db, models.Compra)

@router.get("/{id}", response_model=schemas.CompraResponse)
def read_compra(id: int, db: Session = Depends(database.get_db)):
    compra = crud.get_item(db, models.Compra, id)
    if not compra: raise HTTPException(status_code=404, detail="Compra não encontrada")
    return compra

@router.put("/{id}", response_model=schemas.CompraResponse)
def update_compra(id: int, compra: schemas.CompraCreate, db: Session = Depends(database.get_db)):
    return crud.update_item(db, models.Compra, id, compra.dict())

@router.delete("/{id}")
def delete_compra(id: int, db: Session = Depends(database.get_db)):
    crud.delete_item(db, models.Compra, id)
    return {"message": "Compra excluída"}

@router.delete("/")
def delete_all_compras(db: Session = Depends(database.get_db)):
    crud.delete_all(db, models.Compra)
    return {"message": "Todas as compras excluídas"}