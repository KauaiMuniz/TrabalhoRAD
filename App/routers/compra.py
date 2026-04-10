from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from App import crud, schemas, database

router = APIRouter(prefix="/vendas", tags=["Vendas"])

@router.post("/", response_model=schemas.VendaResponse)
def create_venda_route(venda: schemas.VendaCreate, db: Session = Depends(database.get_db)):
    # Verifica se o produto existe antes de permitir a venda
    if not crud.get_produto(db, venda.produto_id):
        raise HTTPException(status_code=404, detail="Produto não encontrado")
    return crud.create_venda(db, venda)

@router.get("/", response_model=list[schemas.VendaResponse])
def read_vendas(db: Session = Depends(database.get_db)):
    return crud.get_vendas(db)

@router.get("/{id}", response_model=schemas.VendaResponse)
def read_venda(id: int, db: Session = Depends(database.get_db)):
    venda = crud.get_venda(db, id)
    if not venda:
        raise HTTPException(status_code=404, detail="Venda não encontrada")
    return venda

@router.put("/{id}", response_model=schemas.VendaResponse)
def update_venda_route(id: int, venda: schemas.VendaCreate, db: Session = Depends(database.get_db)):
    return crud.update_venda(db, id, venda)

@router.delete("/{id}")
def delete_venda_route(id: int, db: Session = Depends(database.get_db)):
    crud.delete_venda(db, id)
    return {"message": "Venda excluída"}

@router.delete("/")
def delete_all_vendas_route(db: Session = Depends(database.get_db)):
    crud.delete_all_vendas(db)
    return {"message": "Todas as vendas excluídas"}