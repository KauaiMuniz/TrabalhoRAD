# Usa uma imagem oficial do Python leve
FROM python:3.10-slim

# Define o diretório de trabalho
WORKDIR /code

# Copia os arquivos de dependência e instala
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia todo o projeto
COPY . /code

# Comando para rodar a aplicação
CMD ["uvicorn", "App.main:app", "--host", "0.0.0.0", "--port", "8000"]