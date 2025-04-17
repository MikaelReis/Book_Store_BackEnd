# `python-base` sets up all our shared environment variables
FROM python:3.11-slim as python-base

# python
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    \
    # pip
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100 \
    \
    # poetry
    POETRY_VERSION=1.0.3 \
    POETRY_HOME="/opt/poetry" \
    POETRY_VIRTUALENVS_IN_PROJECT=true \
    POETRY_NO_INTERACTION=1 \
    \
    # paths
    PYSETUP_PATH="/opt/pysetup" \
    VENV_PATH="/opt/pysetup/.venv"

# prepend poetry and venv to path
ENV PATH="$POETRY_HOME/bin:$VENV_PATH/bin:$PATH"

# instala dependências do sistema
RUN apt-get update \
    && apt-get install --no-install-recommends -y \
        curl \
        build-essential \
        python3-dev \
        gcc \
        libpq-dev \
    && apt-get clean

# garante que "python" aponte para "python3"
RUN ln -s /usr/bin/python3 /usr/bin/python || true

# instala o Poetry (nova forma)
RUN curl -sSL https://install.python-poetry.org | python3 - --version 1.7.1

# define o diretório de trabalho para o projeto Python
WORKDIR $PYSETUP_PATH
COPY poetry.lock pyproject.toml ./

# instala dependências do projeto
RUN poetry install --only main

WORKDIR /app
COPY . /app/

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
