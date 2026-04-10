from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from App import crud, schemas, database

router = APIRouter(prefix="/fornecedores", tags=["Fornecedores"])

@router.post("/", response_model=schemas.FornecedorResponse)
def create_fornecedor_route(fornecedor: schemas.FornecedorCreate, db: Session = Depends(database.get_db)):
    return crud.create_fornecedor(db, fornecedor)

@router.get("/", response_model=list[schemas.FornecedorResponse])
def read_fornecedores(db: Session = Depends(database.get_db)):
    return crud.get_fornecedores(db)

@router.get("/{id}", response_model=schemas.FornecedorResponse)
def read_fornecedor(id: int, db: Session = Depends(database.get_db)):
    fornecedor = crud.get_fornecedor(db, id)
    if not fornecedor:
        raise HTTPException(status_code=404, detail="Fornecedor não encontrado")
    return fornecedor

@router.put("/{id}", response_model=schemas.FornecedorResponse)
def update_fornecedor_route(id: int, fornecedor: schemas.FornecedorCreate, db: Session = Depends(database.get_db)):
    return crud.update_fornecedor(db, id, fornecedor)

@router.delete("/{id}")
def delete_fornecedor_route(id: int, db: Session = Depends(database.get_db)):
    crud.delete_fornecedor(db, id)
    return {"message": "Fornecedor excluído"}

@router.delete("/")
def delete_all_fornecedores_route(db: Session = Depends(database.get_db)):
    crud.delete_all_fornecedores(db)
    return {"message": "Todos os fornecedores excluídos"}