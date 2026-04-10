# API - Loja de Roupas (CRUD) 👕👖

Projeto acadêmico desenvolvido para a disciplina de **RAD - Desenvolvimento Rápido de Aplicações em Python**. O sistema consiste em uma API RESTful completa para o gerenciamento de uma Loja de Roupas, implementando operações de CRUD (Create, Read, Update, Delete).

## 🚀 Tecnologias Utilizadas

* **Linguagem:** Python 3.10+
* **Framework API:** FastAPI
* **Validação de Dados:** Pydantic
* **ORM:** SQLAlchemy
* **Banco de Dados:** PostgreSQL
* **Servidor ASGI:** Uvicorn
* **Containerização:** Docker e Docker Compose

## 📦 Módulos do Sistema

O sistema está dividido em 5 módulos principais, cada um contendo as seguintes operações: Inserir, Listar, Consultar (por ID), Alterar, Excluir um item e Excluir tudo.

1.  **Cliente:** Gestão de clientes (Nome e Email).
2.  **Fornecedor:** Gestão de fornecedores parceiros (Nome e CNPJ).
3.  **Produto:** Catálogo de roupas da loja (Nome e Preço).
4.  **Compra:** Registro de abastecimento de estoque (Associação com Produto).
5.  **Venda:** Registro de saída de mercadorias (Associação com Produto).

## 📂 Estrutura do Projeto

```text
Trabalho/
├── App/
│   ├── routers/
│   │   ├── cliente.py
│   │   ├── compra.py
│   │   ├── fornecedor.py
│   │   ├── produto.py
│   │   └── venda.py
│   ├── crud.py          # Lógica de banco de dados
│   ├── database.py      # Conexão com o PostgreSQL
│   ├── main.py          # Inicialização do FastAPI
│   ├── models.py        # Modelos do SQLAlchemy (Tabelas)
│   └── schemas.py       # Validação de dados (Pydantic)
├── docker-compose.yml   # Orquestração do Banco + API
├── Dockerfile           # Imagem da aplicação
├── requirements.txt     # Dependências do Python
└── README.md            # Documentação
```
## 🛠️ Como Executar o Projeto

O projeto foi construído para ser facilmente executado utilizando **Docker** (recomendado, pois já configura o banco de dados e a API juntos), mas também pode ser rodado **Localmente** no seu próprio ambiente Python.

### Opção 1: Executando via Docker (Recomendado)

Esta opção exige apenas que você tenha o [Docker Desktop](https://www.docker.com/products/docker-desktop/) instalado na sua máquina. O Docker se encarregará de baixar o PostgreSQL, criar o banco de dados e iniciar a API.

1. Abra o terminal na raiz do projeto (onde está o arquivo `docker-compose.yml`).
2. Execute o comando para construir e subir os containers:
   ```bash
   docker-compose up --build