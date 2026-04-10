from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from App import crud, models, schemas, database

router = APIRouter(prefix="/fornecedores", tags=["Fornecedores"])

@router.post("/", response_model=schemas.FornecedorResponse)
def create_fornecedor(fornecedor: schemas.FornecedorCreate, db: Session = Depends(database.get_db)):
    return crud.create_item(db, models.Fornecedor, fornecedor.dict())

@router.get("/", response_model=list[schemas.FornecedorResponse])
def read_fornecedores(db: Session = Depends(database.get_db)):
    return crud.get_items(db, models.Fornecedor)

@router.get("/{id}", response_model=schemas.FornecedorResponse)
def read_fornecedor(id: int, db: Session = Depends(database.get_db)):
    fornecedor = crud.get_item(db, models.Fornecedor, id)
    if not fornecedor: raise HTTPException(status_code=404, detail="Fornecedor não encontrado")
    return fornecedor

@router.put("/{id}", response_model=schemas.FornecedorResponse)
def update_fornecedor(id: int, fornecedor: schemas.FornecedorCreate, db: Session = Depends(database.get_db)):
    return crud.update_item(db, models.Fornecedor, id, fornecedor.dict())

@router.delete("/{id}")
def delete_fornecedor(id: int, db: Session = Depends(database.get_db)):
    crud.delete_item(db, models.Fornecedor, id)
    return {"message": "Fornecedor excluído"}

@router.delete("/")
def delete_all_fornecedores(db: Session = Depends(database.get_db)):
    crud.delete_all(db, models.Fornecedor)
    return {"message": "Todos os fornecedores excluídos"}