from pydantic import BaseModel

# --- Schemas Base ---
class BasePessoa(BaseModel):
    nome: str

# --- Cliente ---
class ClienteCreate(BasePessoa):
    email: str

class ClienteResponse(ClienteCreate):
    id: int
    class Config: orm_mode = True

# --- Fornecedor ---
class FornecedorCreate(BasePessoa):
    cnpj: str

class FornecedorResponse(FornecedorCreate):
    id: int
    class Config: orm_mode = True

# --- Produto ---
class ProdutoCreate(BaseModel):
    nome: str
    preco: float

class ProdutoResponse(ProdutoCreate):
    id: int
    class Config: orm_mode = True

# --- Compra ---
class CompraCreate(BaseModel):
    produto_id: int
    quantidade: int

class CompraResponse(CompraCreate):
    id: int
    class Config: orm_mode = True

# --- Venda ---
class VendaCreate(BaseModel):
    produto_id: int
    quantidade: int

class VendaResponse(VendaCreate):
    id: int
    class Config: orm_mode = True