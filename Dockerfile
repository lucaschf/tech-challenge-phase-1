# Use a imagem oficial do Python 3.12
FROM python:3.12.3-slim-bookworm

# Evita que o Python crie arquivos .pyc
ENV PYTHONDONTWRITEBYTECODE 1

# Evita que o Python armazene em buffer stdout e stderr
ENV PYTHONUNBUFFERED 1

# Define o diretório de trabalho para /src
WORKDIR /src

# Instala as dependências do sistema
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        build-essential \
        libpq-dev \
        && rm -rf /var/lib/apt/lists/*

# Copia apenas os arquivos necessários para a instalação do Poetry
COPY pyproject.toml poetry.lock ./

# Instala o Poetry e as dependências do projeto
RUN pip install --no-cache-dir poetry \
    && python -m venv .venv  \
    && . .venv/bin/activate \
    && poetry install --no-interaction --no-ansi --only main \
    && poetry self add poetry-dotenv-plugin

# Copia o restante do código da aplicação para o contêiner
COPY . .

# Expõe a porta especificada para o FastAPI
EXPOSE $PORT

# Inicia a aplicação com Uvicorn em modo de produção, usando referências de variáveis de ambiente
CMD ["poetry", "run", "uvicorn", "src.adapter.driver.api:app", "--host", "0.0.0.0", "--port", "80"]
