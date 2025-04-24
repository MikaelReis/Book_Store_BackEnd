FROM python:3.11-slim

# Instala dependências do sistema
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    git \
    && rm -rf /var/lib/apt/lists/*

# Configura o ambiente
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on

# Instala Poetry
RUN pip install --upgrade pip && \
    pip install poetry==1.8.4

WORKDIR /app

# Copia e instala dependências
COPY pyproject.toml poetry.lock ./

# Instala todas as dependências, incluindo grupo 'dev'
RUN poetry config virtualenvs.create false && \
    poetry install --no-interaction --no-ansi

# Copia o restante do código
COPY . .

# Expondo a porta
EXPOSE 8000

# Comando padrão
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

