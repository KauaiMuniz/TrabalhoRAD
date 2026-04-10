from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from App import crud, models, schemas, database

router = APIRouter(prefix="/clientes", tags=["Clientes"])

@router.post("/", response_model=schemas.ClienteResponse) # 1. Inserir
def create_cliente(cliente: schemas.ClienteCreate, db: Session = Depends(database.get_db)):
    return crud.create_item(db, models.Cliente, cliente.dict())

@router.get("/", response_model=list[schemas.ClienteResponse]) # 2. Listar
def read_clientes(db: Session = Depends(database.get_db)):
    return crud.get_items(db, models.Cliente)

@router.get("/{id}", response_model=schemas.ClienteResponse) # 3. Consultar
def read_cliente(id: int, db: Session = Depends(database.get_db)):
    cliente = crud.get_item(db, models.Cliente, id)
    if not cliente: raise HTTPException(status_code=404, detail="Cliente não encontrado")
    return cliente

@router.put("/{id}", response_model=schemas.ClienteResponse) # 4. Alterar
def update_cliente(id: int, cliente: schemas.ClienteCreate, db: Session = Depends(database.get_db)):
    return crud.update_item(db, models.Cliente, id, cliente.dict())

@router.delete("/{id}") # 5. Excluir um item
def delete_cliente(id: int, db: Session = Depends(database.get_db)):
    crud.delete_item(db, models.Cliente, id)
    return {"message": "Item excluído"}

@router.delete("/") # 6. Excluir tudo
def delete_all_clientes(db: Session = Depends(database.get_db)):
    crud.delete_all(db, models.Cliente)
    return {"message": "Todos os itens excluídos"}