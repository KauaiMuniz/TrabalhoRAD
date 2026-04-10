from sqlalchemy.orm import Session
from . import models, schemas

# ==========================================
# CLIENTE CRUD
# ==========================================
def create_cliente(db: Session, cliente: schemas.ClienteCreate):
    db_cliente = models.Cliente(**cliente.dict())
    db.add(db_cliente)
    db.commit()
    db.refresh(db_cliente)
    return db_cliente

def get_clientes(db: Session):
    return db.query(models.Cliente).all()

def get_cliente(db: Session, cliente_id: int):
    return db.query(models.Cliente).filter(models.Cliente.id == cliente_id).first()

def update_cliente(db: Session, cliente_id: int, cliente: schemas.ClienteCreate):
    db.query(models.Cliente).filter(models.Cliente.id == cliente_id).update(cliente.dict())
    db.commit()
    return get_cliente(db, cliente_id)

def delete_cliente(db: Session, cliente_id: int):
    db.query(models.Cliente).filter(models.Cliente.id == cliente_id).delete()
    db.commit()

def delete_all_clientes(db: Session):
    db.query(models.Cliente).delete()
    db.commit()


# ==========================================
# PRODUTO CRUD
# ==========================================
def create_produto(db: Session, produto: schemas.ProdutoCreate):
    db_produto = models.Produto(**produto.dict())
    db.add(db_produto)
    db.commit()
    db.refresh(db_produto)
    return db_produto

def get_produtos(db: Session):
    return db.query(models.Produto).all()

def get_produto(db: Session, produto_id: int):
    return db.query(models.Produto).filter(models.Produto.id == produto_id).first()

def update_produto(db: Session, produto_id: int, produto: schemas.ProdutoCreate):
    db.query(models.Produto).filter(models.Produto.id == produto_id).update(produto.dict())
    db.commit()
    return get_produto(db, produto_id)

def delete_produto(db: Session, produto_id: int):
    db.query(models.Produto).filter(models.Produto.id == produto_id).delete()
    db.commit()

def delete_all_produtos(db: Session):
    db.query(models.Produto).delete()
    db.commit()


# ==========================================
# FORNECEDOR CRUD
# ==========================================
def create_fornecedor(db: Session, fornecedor: schemas.FornecedorCreate):
    db_fornecedor = models.Fornecedor(**fornecedor.dict())
    db.add(db_fornecedor)
    db.commit()
    db.refresh(db_fornecedor)
    return db_fornecedor

def get_fornecedores(db: Session):
    return db.query(models.Fornecedor).all()

def get_fornecedor(db: Session, fornecedor_id: int):
    return db.query(models.Fornecedor).filter(models.Fornecedor.id == fornecedor_id).first()

def update_fornecedor(db: Session, fornecedor_id: int, fornecedor: schemas.FornecedorCreate):
    db.query(models.Fornecedor).filter(models.Fornecedor.id == fornecedor_id).update(fornecedor.dict())
    db.commit()
    return get_fornecedor(db, fornecedor_id)

def delete_fornecedor(db: Session, fornecedor_id: int):
    db.query(models.Fornecedor).filter(models.Fornecedor.id == fornecedor_id).delete()
    db.commit()

def delete_all_fornecedores(db: Session):
    db.query(models.Fornecedor).delete()
    db.commit()


# ==========================================
# COMPRA CRUD
# ==========================================
def create_compra(db: Session, compra: schemas.CompraCreate):
    db_compra = models.Compra(**compra.dict())
    db.add(db_compra)
    db.commit()
    db.refresh(db_compra)
    return db_compra

def get_compras(db: Session):
    return db.query(models.Compra).all()

def get_compra(db: Session, compra_id: int):
    return db.query(models.Compra).filter(models.Compra.id == compra_id).first()

def update_compra(db: Session, compra_id: int, compra: schemas.CompraCreate):
    db.query(models.Compra).filter(models.Compra.id == compra_id).update(compra.dict())
    db.commit()
    return get_compra(db, compra_id)

def delete_compra(db: Session, compra_id: int):
    db.query(models.Compra).filter(models.Compra.id == compra_id).delete()
    db.commit()

def delete_all_compras(db: Session):
    db.query(models.Compra).delete()
    db.commit()


# ==========================================
# VENDA CRUD
# ==========================================
def create_venda(db: Session, venda: schemas.VendaCreate):
    db_venda = models.Venda(**venda.dict())
    db.add(db_venda)
    db.commit()
    db.refresh(db_venda)
    return db_venda

def get_vendas(db: Session):
    return db.query(models.Venda).all()

def get_venda(db: Session, venda_id: int):
    return db.query(models.Venda).filter(models.Venda.id == venda_id).first()

def update_venda(db: Session, venda_id: int, venda: schemas.VendaCreate):
    db.query(models.Venda).filter(models.Venda.id == venda_id).update(venda.dict())
    db.commit()
    return get_venda(db, venda_id)

def delete_venda(db: Session, venda_id: int):
    db.query(models.Venda).filter(models.Venda.id == venda_id).delete()
    db.commit()

def delete_all_vendas(db: Session):
    db.query(models.Venda).delete()
    db.commit()