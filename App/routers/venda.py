from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from App import crud, models, schemas, database

router = APIRouter(prefix="/vendas", tags=["Vendas"])

@router.post("/", response_model=schemas.VendaResponse)
def create_venda(venda: schemas.VendaCreate, db: Session = Depends(database.get_db)):
    # Validação extra: verificar se o produto existe antes de registrar a venda
    produto = crud.get_item(db, models.Produto, venda.produto_id)
    if not produto: raise HTTPException(status_code=404, detail="Produto não encontrado")
    return crud.create_item(db, models.Venda, venda.dict())

@router.get("/", response_model=list[schemas.VendaResponse])
def read_vendas(db: Session = Depends(database.get_db)):
    return crud.get_items(db, models.Venda)

@router.get("/{id}", response_model=schemas.VendaResponse)
def read_venda(id: int, db: Session = Depends(database.get_db)):
    venda = crud.get_item(db, models.Venda, id)
    if not venda: raise HTTPException(status_code=404, detail="Venda não encontrada")
    return venda

@router.put("/{id}", response_model=schemas.VendaResponse)
def update_venda(id: int, venda: schemas.VendaCreate, db: Session = Depends(database.get_db)):
    return crud.update_item(db, models.Venda, id, venda.dict())

@router.delete("/{id}")
def delete_venda(id: int, db: Session = Depends(database.get_db)):
    crud.delete_item(db, models.Venda, id)
    return {"message": "Venda excluída"}

@router.delete("/")
def delete_all_vendas(db: Session = Depends(database.get_db)):
    crud.delete_all(db, models.Venda)
    return {"message": "Todas as vendas excluídas"}