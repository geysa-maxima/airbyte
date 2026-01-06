FROM python:3.10-slim

# Instala dependências do SO (ajuste conforme necessário)
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libaio1 \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Copia arquivos do projeto
COPY . /app

# Instala dependências Python
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

ENV PYTHONUNBUFFERED=1

# entrypoint: o módulo entrypoint do pacote
ENTRYPOINT ["python", "-m", destination_oracle_custom01.entrypoint]