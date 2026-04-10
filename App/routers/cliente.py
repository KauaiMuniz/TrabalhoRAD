from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from App import crud, models, schemas, database

router = APIRouter(prefix="/clientes", tags=["Clientes"])

@router.post("/", response_model=schemas.ClienteResponse) # 1. Inserir
def create_cliente_route(cliente: schemas.ClienteCreate, db: Session = Depends(database.get_db)):
    # Chama a função específica do crud.py passando apenas o db e o schema
    return crud.create_cliente(db, cliente)

@router.get("/", response_model=list[schemas.ClienteResponse]) # 2. Listar
def read_clientes(db: Session = Depends(database.get_db)):
    # Chama a função get_clientes
    return crud.get_clientes(db)

@router.get("/{id}", response_model=schemas.ClienteResponse) # 3. Consultar
def read_cliente(id: int, db: Session = Depends(database.get_db)):
    cliente = crud.get_cliente(db, id)
    if not cliente:
        raise HTTPException(status_code=404, detail="Cliente não encontrado")
    return cliente

@router.put("/{id}", response_model=schemas.ClienteResponse) # 4. Alterar
def update_cliente_route(id: int, cliente: schemas.ClienteCreate, db: Session = Depends(database.get_db)):
    return crud.update_cliente(db, id, cliente)

@router.delete("/{id}") # 5. Excluir um item
def delete_cliente_route(id: int, db: Session = Depends(database.get_db)):
    crud.delete_cliente(db, id)
    return {"message": "Cliente excluído"}

@router.delete("/") # 6. Excluir tudo
def delete_all_clientes_route(db: Session = Depends(database.get_db)):
    crud.delete_all_clientes(db)
    return {"message": "Todos os clientes excluídos"}